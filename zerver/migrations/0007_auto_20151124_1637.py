# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0006_auto_20151124_1636'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='realm',
            options={'permissions': (('administer', 'Administer a realm'), ('api_super_user', 'Can send messages as other users for mirroring'))},
        ),
        migrations.AddField(
            model_name='message',
            name='has_attachment',
            field=models.BooleanField(default=False, db_index=True),
        ),
        migrations.AddField(
            model_name='message',
            name='has_image',
            field=models.BooleanField(default=False, db_index=True),
        ),
        migrations.AddField(
            model_name='message',
            name='has_link',
            field=models.BooleanField(default=False, db_index=True),
        ),
        migrations.AddField(
            model_name='pushdevicetoken',
            name='ios_app_id',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='realm',
            name='invite_by_admins_only',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='realm',
            name='invite_required',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='realm',
            name='mandatory_topics',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='realm',
            name='name_changes_disabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='realm',
            name='show_digest_email',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='audible_notifications',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='desktop_notifications',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_all_public_streams',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_events_register_stream',
            field=models.ForeignKey(related_name='+', to='zerver.Stream', null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_sending_stream',
            field=models.ForeignKey(related_name='+', to='zerver.Stream', null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='enable_stream_desktop_notifications',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='enable_stream_sounds',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='left_side_userlist',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='twenty_four_hour_time',
            field=models.BooleanField(default=False),
        ),
    ]
