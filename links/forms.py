# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML
from crispy_forms.bootstrap import Field, FormActions


from .models import Link


class LinkForm(forms.ModelForm):
    description = forms.CharField(
        max_length=750,
        help_text=_("A short description.  Please limit to 750 cahracters."),
        widget=forms.Textarea
    )

    class Meta:
        model = Link
        fields = ['title', 'link', 'description']

    def __init__(self, *args, **kwargs):
        super(LinkForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'link-form'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('title'),
            Field('link'),
            Field('description'),
            FormActions(
                Submit('submit', _('Save'), css_class='btn-success'),
                HTML(
                    "<a class='btn btn-default' href='{% url \"home\" %}'>Cancel</a>")
            )
        )
