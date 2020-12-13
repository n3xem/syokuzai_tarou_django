from django import forms
from refrigerator.models import *
from django.contrib.admin import widgets
import bootstrap_datepicker_plus as datetimepicker
from django.core.exceptions import ValidationError
import os

#recipe_checkbox
class RecipeForm(forms.Form):
    def __init__(self, user, foods=[], *args, **kwargs):
        super(RecipeForm, self).__init__(*args,**kwargs)
        self.fields['foods'] = forms.MultipleChoiceField(
            label = "",
            choices = [(item.id,item.foodset) for item in foods],
            widget = forms.CheckboxSelectMultiple(),
            initial = 0
        )