from django.db import models
#from review_app.auth.models import ReviewUser

# Create your models here.

class ReviewSession(models.Model):
#    facilitator = models.ForeignKey(ReviewUser, related_name='+')
    review_notes_url = models.URLField(max_length=4096)
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    
class FeedbackItem(models.Model):
    session = models.ForeignKey(ReviewSession, related_name='feedback')
    who = models.CharField(max_length=50)
    when = models.DateTimeField()
    text = models.CharField(max_length=4096)


