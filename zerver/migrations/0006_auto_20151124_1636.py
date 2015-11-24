# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0005_auto_20150920_1340'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='realm',
            options={'permissions': (('administer', 'Administer a realm'),)},
        ),
        migrations.RemoveField(
            model_name='message',
            name='has_attachment',
        ),
        migrations.RemoveField(
            model_name='message',
            name='has_image',
        ),
        migrations.RemoveField(
            model_name='message',
            name='has_link',
        ),
        migrations.RemoveField(
            model_name='pushdevicetoken',
            name='ios_app_id',
        ),
        migrations.RemoveField(
            model_name='realm',
            name='invite_by_admins_only',
        ),
        migrations.RemoveField(
            model_name='realm',
            name='invite_required',
        ),
        migrations.RemoveField(
            model_name='realm',
            name='mandatory_topics',
        ),
        migrations.RemoveField(
            model_name='realm',
            name='name_changes_disabled',
        ),
        migrations.RemoveField(
            model_name='realm',
            name='show_digest_email',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='audible_notifications',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='desktop_notifications',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='default_all_public_streams',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='default_events_register_stream',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='default_sending_stream',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='enable_stream_desktop_notifications',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='enable_stream_sounds',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='left_side_userlist',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='twenty_four_hour_time',
        ),
    ]
