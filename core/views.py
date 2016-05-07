# from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from links.models import Link


class HomePageView(ListView):
    model = Link
    template_name = "home.html"
    paginate_by = 50

    def get_queryset(self):
        return Link.objects.active()

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context
