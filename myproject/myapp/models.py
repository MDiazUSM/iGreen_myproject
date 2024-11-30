from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    score = models.IntegerField(default=0)

class QRCode(models.Model):
    code = models.CharField(max_length=100, unique=True)
    points = models.IntegerField(default=0)
    scans = models.IntegerField(default=0)

class ScanRecord(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    qr_code = models.ForeignKey(QRCode, on_delete=models.CASCADE)
    scanned_at = models.DateTimeField(auto_now_add=True)

