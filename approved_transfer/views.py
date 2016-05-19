from zerver.decorator import authenticated_json_view, has_request_variables, REQ
from zerver.lib.response import json_error, json_success
from approved_transfer.models import ApprovedTransfer

@authenticated_json_view
@has_request_variables
def approve_transfer(request, user_profile, status=REQ(default="transfer")):
    if user_profile.realm.domain != "mit.edu":
        return json_error("Only valid for MIT realm users")
    ApprovedTransfer.objects.create(user_profile=user_profile, status=status)
    return json_success()
