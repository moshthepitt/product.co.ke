from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import LinkUpdate, LinkAdd

urlpatterns = [
    url(r'^add/$', login_required(LinkAdd.as_view()), name='link_add'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(LinkUpdate.as_view()), name='link_edit'),
]
