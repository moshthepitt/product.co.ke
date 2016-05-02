from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings

from links.models import Link

User = settings.AUTH_USER_MODEL


@python_2_unicode_compatible
class Vote(models.Model):
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    user = models.ForeignKey(User, verbose_name=_("User"))
    link = models.ForeignKey(Link, verbose_name=_("Link"))

    class Meta:
        verbose_name = _("Vote")
        verbose_name_plural = _("Votes")
        unique_together = (("user", "link"),)

    def __str__(self):
        "{} {}".format(self.user.username, self.link)

