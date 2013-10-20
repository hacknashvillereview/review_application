from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from review_app.models import ReviewSession, ReviewUser


@login_required
def protected_method(request):
    """This is a method that requires login"""

    return render_to_response("protected.html",
        {"test": request.user.id},
        context_instance=RequestContext(request))

@login_required
def packages_method(request):

    rUser = ReviewUser.objects.get(user=request.user.id)

    return render_to_response("packages.html",
        {"packages": ReviewSession.objects.filter(facilitator=rUser.id)},
        context_instance=RequestContext(request))


@login_required
def package_method(request, package_id):
    rUser = ReviewUser.objects.get(user=request.user.id)

    review_session = ReviewSession.objects.get(pk=package_id)
    if not rUser.id == review_session.facilitator_id:
        raise PermissionDenied("You do not have access to package %s." % package_id)

    return render_to_response("package.html",
        {"package": review_session},
        context_instance=RequestContext(request))

