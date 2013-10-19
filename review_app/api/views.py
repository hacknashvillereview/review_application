# Create your views here.

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView 
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.settings import api_settings

class ApiRoot(APIView):
    """
    The entry endpoint for the API.
    """

    def get(self, request):
        return Response({
            'hello-world': {
                'helloworld': reverse("helloworld", request=request),
            },
        })

class HelloWorld(APIView):
    """This is just a simple hello world"""

    def get(self, request):
        return Response({"message": "hello world"})

