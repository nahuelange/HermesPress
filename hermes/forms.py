from django import forms
from django.forms.models import ModelForm
from hermes.models import RessourceCollection


class CollectionForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = RessourceCollection
        fields = ['title', 'description',]
