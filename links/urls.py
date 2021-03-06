from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import LinkUpdate, LinkAdd, LinkView, UserLinksView, UserLinkDelete

urlpatterns = [
    url(r'^add/$', login_required(LinkAdd.as_view()), name='link_add'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(LinkUpdate.as_view()), name='link_edit'),
    url(r'^my-submissions/$', login_required(UserLinksView.as_view()), name='user_links'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(UserLinkDelete.as_view()), name='user_delete_link'),
    url(r'^(?P<pk>\d+)/$', LinkView.as_view(), name='link_detail'),
]
