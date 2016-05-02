from django.views.generic.base import TemplateView

from links.models import Link


class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['links'] = Link.objects.active()
        return context
