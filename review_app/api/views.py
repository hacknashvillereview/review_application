# Create your views here.

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.settings import api_settings
from api.serializers import ReviewSessionSerializer, FeedbackItemSerializer
from review_app.models import ReviewSession, FeedbackItem


class ApiRoot(APIView):
    """
    The entry endpoint for the API.
    """

    def get(self, request):
        return Response({
            'hello-world': {
                'helloworld': reverse("helloworld", request=request),
            },
            'reviewSession': {
                'reviewSession': reverse("reviewSession", request=request),
                },
            'feedback': {
                'feedback': reverse("feedback", request=request),
            },
        })


class HelloWorld(APIView):
    """This is just a simple hello world"""

    def get(self, request):
        return Response({"message": "hello world"})


class ReviewSessionList(generics.ListCreateAPIView):
    queryset = ReviewSession.objects.all()
    serializer_class = ReviewSessionSerializer


class ReviewSessionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewSession.objects.all()
    serializer_class = ReviewSessionSerializer


class FeedbackItemList(generics.ListCreateAPIView):
    queryset = FeedbackItem.objects.all()
    serializer_class = FeedbackItemSerializer


class FeedbackItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FeedbackItem.objects.all()
    serializer_class = FeedbackItemSerializer
