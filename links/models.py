from __future__ import unicode_literals
from urlparse import urlparse

from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class LinkManager(models.Manager):

    def get_queryset(self):
        return super(LinkManager, self).get_queryset()

    def active(self):
        return self.get_queryset().filter(active=True)


@python_2_unicode_compatible
class Link(models.Model):
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    user = models.ForeignKey(User, verbose_name=_("User"))
    link = models.URLField(_("Link"), max_length=2083, blank=False)
    description = models.TextField(_("Description"), blank=True, default="", help_text=_(
        "A short description.  Please limit to 300 cahracters."))
    active = models.BooleanField(_("Active"), default=True)
    ghost = models.BooleanField(_("Ghost"), default=False)  # used to fight spam

    objects = LinkManager()

    class Meta:
        verbose_name = _("Link")
        verbose_name_plural = _("Links")

    def __str__(self):
        return self.link

    @models.permalink
    def get_absolute_url(self):
        return ('')

    @property
    def domain(self):
        return urlparse(self.url).netloc
