import logging
from zerver.middleware import async_request_restart

current_handler_id = 0
handlers = {}

def get_handler_by_id(handler_id):
    return handlers[handler_id]

def allocate_handler_id(handler):
    global current_handler_id
    handler.handler_id = current_handler_id
    handlers[current_handler_id] = handler
    current_handler_id += 1
    return handler.handler_id

def clear_handler_by_id(handler_id):
    del handlers[handler_id]

def handler_stats_string():
    return "%s handlers, latest ID %s" % (len(handlers), current_handler_id)

known_queue_ids = {}
def record_queue_id(queue_id, user_profile_id):
    known_queue_ids[queue_id] = user_profile_id

def fetch_queue_id(queue_id):
    return known_queue_ids.get(queue_id)

def finish_handler(handler_id, event_queue_id, response, apply_markdown):
    err_msg = "Got error finishing handler for queue %s" % (event_queue_id,)
    try:
        # We call async_request_restart here in case we are
        # being finished without any events (because another
        # get_events request has supplanted this request)
        handler = get_handler_by_id(handler_id)
        request = handler._request
        async_request_restart(request)
        handler.zulip_finish(response, request, apply_markdown)
    except IOError as e:
        if e.message != 'Stream is closed':
            logging.exception(err_msg)
    except AssertionError as e:
        if e.message != 'Request closed':
            logging.exception(err_msg)
    except Exception:
        logging.exception(err_msg)

def process_events_response(response):
    try:
        handler = get_handler_by_id(response["handler_id"])
        request = handler._request
        if "extra_log_data" in response:
            request._log_data['extra'] = response["extra_log_data"]

        if response["response"].get("queue_id"):
            # If we are returning to the user a new queue we allocated
            record_queue_id(response["queue_id"], request.user.id)
        finish_handler(response["handler_id"], response["queue_id"],
                       response["response"], response["apply_markdown"])
        return response["response"]
    except Exception:
        logging.exception("Error processing event")
        logging.error("Response was " + str(response))
