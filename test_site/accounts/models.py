from django.db import models
import datetime
from django.core.cache import cache
from django.conf import settings

# Create your models here.
class UserProfile(models.Model):


    def last_seen(self):
        return cache.get('seen_%s' % self.user.username)
        

    def online(self):
        if self.last_seen():
            now = datetime.datetime.now()
            if now > self.last_seen() + datetime.timedelta(
                         seconds=settings.USER_ONLINE_TIMEOUT):
                return False
            else:
                return True
        else:
            return False