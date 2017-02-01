from django.db import models

import datetime

from django.utils import timezone

class User(models.Model):
    user_name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('data published')

    def __str__(self):
        return self.user_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Workout(models.Model):
    user = models.ForeignKey(User)
    workout_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.workout_amount