
from django.conf.urls import patterns, include, url

from api.views import *

urlpatterns = patterns('api.views',
    url(r'^$', ApiRoot.as_view(), name='api-root'),
)

urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^helloworld/', HelloWorld.as_view(), name='helloworld'),

    url(r'^reviewSession/$', ReviewSessionList.as_view(), name="reviewsession"),
    url(r'^reviewSession/(?P<pk>[0-9]+)/$', ReviewSessionDetail.as_view(), name="reviewsession-detail"),

    url(r'^feedback/$', FeedbackItemList.as_view(), name="feedbackitem"),
    url(r'^feedback/(?P<pk>[0-9]+)/$', FeedbackItemDetail.as_view(), name="feedbackitem-detail"),

    url(r'^user/$', ReviewUserList.as_view(), name="reviewuser"),
    url(r'^user/(?P<pk>[0-9]+)/$', ReviewUserDetail.as_view(), name="reviewuser-detail"),
)

