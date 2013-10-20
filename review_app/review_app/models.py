from django.db import models
from django.contrib.auth.models import User


class ReviewUser(models.Model):

    user = models.OneToOneField(User)

    # foxycart customer id
    customer_id = models.IntegerField()


class ReviewSession(models.Model):
    title = models.CharField(max_length=100)
    facilitator = models.ForeignKey(ReviewUser, related_name='+')
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(blank=True, null=True)
    video_url = models.URLField(max_length=4096)


class Demo(models.Model):
    session = models.ForeignKey(ReviewSession, related_name='demo')
    title = models.CharField(max_length=100)
    review_notes_url = models.URLField(max_length=4096)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(blank=True, null=True)


class FeedbackItem(models.Model):
    demo = models.ForeignKey(Demo, related_name='feedback')
    who = models.CharField(max_length=50)
    when = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=4096)


