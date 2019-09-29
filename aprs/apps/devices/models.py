from django.contrib.auth.models import User
from django.db import models


class Device(models.Model):
    DEVICE_STATUS_OPTIONS = (
        ('active', 'Active'),
        ('', 'Inactive'),
    )
    owner = models.ForeignKey(User, related_name="devices", on_delete=models.PROTECT)
    name = models.CharField(max_length=30)
    status = models.CharField(max_length=8, choices=DEVICE_STATUS_OPTIONS, default='')
    last_communicated_time = models.DateTimeField(null=True)