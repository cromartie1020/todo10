from django import forms
from .models import Envelope

class EnvelopeForm(forms.ModelForm):
    class Meta:
        model=Envelope
        fields='__all__'