
from django.db import models
from zerver.models import UserProfile

class ApprovedTransfer(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    status = models.CharField(default="transfer", max_length=20)
