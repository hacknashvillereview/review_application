from django.contrib import admin
from models import ReviewUser, ReviewSession, FeedbackItem

admin.site.register((ReviewUser, FeedbackItem, ReviewSession))
