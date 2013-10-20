# Create your views here.

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework import generics, filters
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.settings import api_settings
from api.serializers import ReviewSessionSerializer, FeedbackItemSerializer, ReviewUserSerializer, DemoSerializer
from review_app.models import ReviewSession, FeedbackItem, ReviewUser, Demo


class ApiRoot(APIView):
    """
    The entry endpoint for the API.
    """

    def get(self, request):
        return Response({
            'reviewSession': {
                'reviewSession': reverse("reviewsession", request=request),
                },
            'demo': {
                'demo': reverse("demo", request=request),
            },
            'feedback': {
                'feedback': reverse("feedbackitem", request=request),
            },
            'user': {
                'user': reverse("reviewuser", request=request),
            },
        })


class HelloWorld(APIView):
    """This is just a simple hello world"""

    def get(self, request):
        return Response({"message": "hello world"})


class ReviewSessionList(generics.ListCreateAPIView):
    queryset = ReviewSession.objects.all()
    serializer_class = ReviewSessionSerializer
    filter_fields = ('facilitator',)


class ReviewSessionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewSession.objects.all()
    serializer_class = ReviewSessionSerializer


class DemoList(generics.ListCreateAPIView):
    queryset = Demo.objects.all()
    serializer_class = DemoSerializer
    filter_fields = ('session',)


class DemoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Demo.objects.all()
    serializer_class = DemoSerializer


class FeedbackItemList(generics.ListCreateAPIView):
    queryset = FeedbackItem.objects.all()
    serializer_class = FeedbackItemSerializer
    filter_fields = ('demo', 'who',)


class FeedbackItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FeedbackItem.objects.all()
    serializer_class = FeedbackItemSerializer


class ReviewUserList(generics.ListAPIView):
    queryset = ReviewUser.objects.all()
    serializer_class = ReviewUserSerializer


class ReviewUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewUser.objects.all()
    serializer_class = ReviewUserSerializer

