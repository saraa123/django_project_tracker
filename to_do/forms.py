from django import forms
from .models import Item, Feature, Feedback

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('Issue',)

class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ("name", )

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('feedback', 'name', )
