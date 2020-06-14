from django import forms
from .models import BandRequest, CensorVote


class BandRequestForm(forms.ModelForm):
    class Meta:
        model = BandRequest
        fields = ('band_name', 'request_text', 'timeslot')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['band_name'].widget.attrs.update({'class':'form-control'})
        self.fields['request_text'].widget.attrs.update({'class':'form-control'})
        self.fields['timeslot'].widget.attrs.update({'class':'form-control'})


class CensorVoteForm(forms.ModelForm):

    class Meta(object):
        model = CensorVote
        fields = '__all__'
        widgets = {
            'band_request': forms.HiddenInput(),
            'censor': forms.HiddenInput(),
            'vote': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
        }