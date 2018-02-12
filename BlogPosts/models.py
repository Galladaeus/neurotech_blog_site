from django.db import models
from django.utils import timezone

import datetime


# Full blog post information
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now=True)
    content = models.TextField

    # Check whether post is older than a month
    @staticmethod
    def old_post(self):
        now = timezone.now()
        return now - datetime.timedelta(months=1) <= self.pub_date <= now