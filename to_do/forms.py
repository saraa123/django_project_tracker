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
        name = forms.CharField(label='name', max_length=30)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('feedback', 'name', )
        name = forms.CharField(label='name', max_length=30)
        feedback = forms.CharField(label='feedback', max_length=200)        
