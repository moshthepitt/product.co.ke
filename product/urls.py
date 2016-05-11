from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
from django.views.generic.base import TemplateView
from django.conf import settings

from core.views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^links/', include('links.urls', namespace='links')),
    url(r'^django-messages', TemplateView.as_view(template_name="django_messages.html"),
        name='django_messages'),
    url(r'^page/', include('django.contrib.flatpages.urls')),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
    ]
