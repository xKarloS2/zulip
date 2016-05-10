from zerver.decorator import authenticated_json_view, has_request_variables
from zerver.lib.response import json_error, json_success
from approved_transfer.models import ApprovedTransfer

@authenticated_json_view
@has_request_variables
def approve_transfer(request, user_profile):
    if user_profile.realm.domain != "zulip.com":
        return json_error("Only valid for MIT realm users")
    ApprovedTransfer.objects.create(user_profile=user_profile)
    return json_success()
