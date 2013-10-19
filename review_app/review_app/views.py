
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

@login_required
def protected_method(request):
    """This is a method that requires login"""

    return render_to_response("protected.html",
        {"test": "test value"},
        context_instance=RequestContext(request))
