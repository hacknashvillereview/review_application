from review_app.models import ReviewSession, FeedbackItem
from rest_framework import serializers


class ReviewSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewSession


class FeedbackItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FeedbackItem
