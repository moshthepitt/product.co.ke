from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import LinkUpdate, LinkAdd, LinkView, UserLinksView

urlpatterns = [
    url(r'^add/$', login_required(LinkAdd.as_view()), name='link_add'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(LinkUpdate.as_view()), name='link_edit'),
    url(r'^my-submissions/$', UserLinksView.as_view(), name='user_links'),
    url(r'^(?P<pk>\d+)/$', LinkView.as_view(), name='link_detail'),
]
