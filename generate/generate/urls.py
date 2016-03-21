from django.conf.urls import patterns, include, url
from django.contrib import admin

from authentication.views import ObtainAuthToken
from authentication.views import CheckSession

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^api/v1/', include('narwhals.urls', namespace='v1')),
    url(r'^api-token-auth/', ObtainAuthToken.as_view()),
    url(r'^check-session/', CheckSession.as_view()),
)
