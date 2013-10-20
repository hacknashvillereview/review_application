
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from review_app.models import ReviewSession


@login_required
def protected_method(request):
    """This is a method that requires login"""

    return render_to_response("protected.html",
        {"test": request.user.id},
        context_instance=RequestContext(request))

@login_required
def packages_method(request):

    return render_to_response("packages.html",
        {"packages": ReviewSession.objects.filter(facilitator=request.user.id)},
        context_instance=RequestContext(request))
