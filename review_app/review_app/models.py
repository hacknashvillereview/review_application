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
    youtube_id = models.CharField(max_length=20)


def calc_offset(offset):
    s = offset.seconds
    hours, remainder = divmod(s, 3600)
    minutes, seconds = divmod(remainder, 60)
    return (hours, minutes, seconds)


class Demo(models.Model):
    session = models.ForeignKey(ReviewSession, related_name='demo')
    title = models.CharField(max_length=100)
    review_notes_url = models.URLField(max_length=4096)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(blank=True, null=True)

    @property
    def start_offset(self):
        offset = self.start - self.session.start
        return "%02d:%02d:%02d" % (calc_offset(offset))

    @property
    def end_offset(self):
        offset = self.end - self.session.start
        return "%02d:%02d:%02d" % (calc_offset(offset))


class FeedbackItem(models.Model):
    demo = models.ForeignKey(Demo, related_name='feedback')
    who = models.CharField(max_length=50)
    when = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=4096)

    @property
    def offset(self):
        offset = self.when - self.demo.session.start
        return "%02d:%02d:%02d" % (calc_offset(offset))





