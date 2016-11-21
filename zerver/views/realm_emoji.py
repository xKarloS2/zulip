from __future__ import absolute_import

from django.http import HttpRequest, HttpResponse
from django.core.exceptions import ValidationError

from zerver.decorator import has_request_variables, REQ, require_realm_admin
from zerver.lib.response import json_success, json_error
from zerver.lib.actions import check_add_realm_emoji, do_remove_realm_emoji
from zerver.models import UserProfile

from six import text_type

def list_emoji(request, user_profile):
    # type: (HttpRequest, UserProfile) -> HttpResponse
    return json_success({'emoji': user_profile.realm.get_emoji()})

@has_request_variables
def upload_emoji(request, user_profile, name=REQ(), url=REQ()):
    # type: (HttpRequest, UserProfile, text_type, text_type) -> HttpResponse
    try:
        check_add_realm_emoji(user_profile.realm, name, url)
    except ValidationError as e:
        return json_error(e.messages[0])
    return json_success()

def delete_emoji(request, user_profile, emoji_name):
    # type: (HttpRequest, UserProfile, text_type) -> HttpResponse
    do_remove_realm_emoji(user_profile.realm, emoji_name)
    return json_success()
