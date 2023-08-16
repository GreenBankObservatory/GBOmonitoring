import datetime

from crispy_forms.bootstrap import AppendedText, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Submit

from django import forms


MAX_TIME_SPAN = datetime.timedelta(days=365)

# https://getbootstrap.com/docs/4.6/components/forms/
# https://getbootstrap.com/docs/5.0/examples/sidebars/#
# https://getbootstrap.com/docs/4.1/utilities/flex/


class QueryFormHelper(FormHelper):
    layout = Div(
        Div(
            Div("start", css_class="col"),
            css_class="row",
        ),
        Div(
            Div("end", css_class="col"),
            css_class="row",
        ),
        FormActions(
            Submit("submit", "Submit"),
            css_class="",
        ),
        css_class="container-fluid filter-form",
    )
    # https://django-crispy-forms.readthedocs.io/en/latest/crispy_tag_forms.html


class QueryForm(forms.Form):
    start = forms.DateField(
        label="<hr> Start Date",
        required=False,
        widget=forms.TextInput(attrs={"type": "date"}),
    )
    end = forms.DateField(
        label="End Date", required=False, widget=forms.TextInput(attrs={"type": "date"})
    )

    # method for cleaning the data
    def clean(self, num_of_pts=0):
        super().clean()

        start = self.cleaned_data.get("start")
        end = self.cleaned_data.get("end")

        if (end and not start) or (start and not end):
            self.add_error(
                "start", forms.ValidationError("Specify a start and end date")
            )
            self.add_error("end", forms.ValidationError("Specify a start and end date"))

        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = QueryFormHelper()
