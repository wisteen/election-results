from django import forms
from .models import State, LGA, AnnouncedPUResults

class PollingUnitForm(forms.Form):
    state = forms.ModelChoiceField(queryset=State.objects.all(), label='State', required=True)
    lga = forms.ModelChoiceField(queryset=LGA.objects.none(), label='Local Government Area', required=True)

    def __init__(self, *args, **kwargs):
        super(PollingUnitForm, self).__init__(*args, **kwargs)
        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['lga'].queryset = LGA.objects.filter(state_id=state_id).order_by('lga_name')
            except (ValueError, TypeError):
                pass  # Invalid input; ignore and use empty queryset
        else:
            self.fields['lga'].queryset = LGA.objects.none()
            
            
class ResultForm(forms.ModelForm):
    class Meta:
        model = AnnouncedPUResults
        fields = ['polling_unit', 'party_abbreviation', 'party_score']
        widgets = {
            'polling_unit': forms.Select(attrs={'class': 'form-control'}),
            'party_abbreviation': forms.TextInput(attrs={'class': 'form-control'}),
            'party_score': forms.NumberInput(attrs={'class': 'form-control'}),
        }