from django.contrib import admin
from models import ReviewUser, ReviewSession, FeedbackItem, Demo

admin.site.register((ReviewUser, Demo, FeedbackItem, ReviewSession))
