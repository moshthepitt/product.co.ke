from __future__ import unicode_literals
from urlparse import urlparse

from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
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
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.PROTECT)
    title = models.CharField(_("Title"), max_length=255, blank=False)
    link = models.URLField(_("URL"), max_length=2083, blank=False, unique=True)
    description = models.TextField(_("Description"), blank=False, default="", help_text=_(
        "A short description.  Please limit to 750 cahracters."))
    active = models.BooleanField(_("Active"), default=True)
    ghost = models.BooleanField(_("Ghost"), default=False)  # used to fight spam

    objects = LinkManager()

    class Meta:
        verbose_name = _("Link")
        verbose_name_plural = _("Links")
        ordering = ['-created_on']

    def __str__(self):
        return self.link

    def get_absolute_url(self):
        return reverse('links:link_detail', args=[self.pk])

    @property
    def domain(self):
        return urlparse(self.link).netloc
