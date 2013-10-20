from review_app.models import ReviewSession, FeedbackItem, ReviewUser, Demo
from rest_framework import serializers


class ReviewSessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReviewSession


class DemoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Demo


class FeedbackItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FeedbackItem


class ReviewUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReviewUser
        fields = ('id', 'customer_id', 'username')
