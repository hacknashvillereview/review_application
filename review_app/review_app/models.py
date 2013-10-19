from django.db import models
from django.contrib.auth.models import User


class ReviewUser(models.Model):

    user = models.OneToOneField(User)

    # foxycart customer id
    customer_id = models.IntegerField()


class ReviewSession(models.Model):
    facilitator = models.ForeignKey(ReviewUser, related_name='+')
    review_notes_url = models.URLField(max_length=4096)
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)


class FeedbackItem(models.Model):
    session = models.ForeignKey(ReviewSession, related_name='feedback')
    who = models.CharField(max_length=50)
    when = models.DateTimeField()
    text = models.CharField(max_length=4096)


