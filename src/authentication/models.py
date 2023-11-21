from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    phone_number = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(null=True, blank=True, default=timezone.now)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)