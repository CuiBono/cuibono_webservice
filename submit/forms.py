from django import forms

from cuibono.models import Ad

class SubmitAdForm(forms.ModelForm):
    class Meta:
        model = Ad
        exclude = ('ingested',
                   'duplicate',
                  )
