from __future__ import absolute_import
from __future__ import print_function

from django.conf import settings
settings.RUNNING_INSIDE_TORNADO = True
# We must call zerver.lib.tornado_ioloop_logging.instrument_tornado_ioloop
# before we import anything else from our project in order for our
# Tornado load logging to work; otherwise we might accidentally import
# zerver.lib.queue (which will instantiate the Tornado ioloop) before
# this.
from zerver.lib.tornado_ioloop_logging import instrument_tornado_ioloop
instrument_tornado_ioloop()

import django
from django.core.management.base import BaseCommand
from django.utils import translation
import os
import sys
import logging
from tornado import ioloop
from zerver.lib.debug import interactive_debug_listen
from zerver.lib.event_queue import setup_event_queue, process_events_request, \
    add_client_gc_hook,  missedmessage_hook, process_notification
from zerver.lib.queue import setup_tornado_rabbitmq

if settings.USING_RABBITMQ:
    from zerver.lib.queue import get_queue_client

class Command(BaseCommand):
    help = "Starts the Event Queue server."

    def handle(self, **options):
        # setup unbuffered I/O
        sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
        sys.stderr = os.fdopen(sys.stderr.fileno(), 'w', 0)
        interactive_debug_listen()

        if settings.DEBUG:
            logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(levelname)-8s %(message)s')

        translation.activate(settings.LANGUAGE_CODE)
        print("Validating Django models.py...")
        self.validate(display_num_errors=True)
        print("\nDjango version %s" % (django.get_version(),))
        print("Queue server is running")

        queue_client = get_queue_client()
        # Process notifications received via RabbitMQ
        queue_client.register_json_consumer('notify_tornado', process_notification)
        queue_client.register_json_consumer('tornado_to_events', process_events_request)

        try:
            if django.conf.settings.DEBUG:
                ioloop.IOLoop.instance().set_blocking_log_threshold(5)

            setup_event_queue()
            add_client_gc_hook(missedmessage_hook)
            setup_tornado_rabbitmq()
            ioloop.IOLoop.instance().start()
        except KeyboardInterrupt:
            sys.exit(0)
