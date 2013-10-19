from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import api, foxycart

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    # Examples:
    # url(r'^$', 'review_app.views.home', name='home'),
    # url(r'^review_app/', include('review_app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    url(r'^api/', include('api.urls')),

    url(r"^foxycart/", include(foxycart.urls)),

)
