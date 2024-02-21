from django.forms import ModelForm, TextInput, DateInput, NumberInput, EmailInput
from .models import PersonContact


class PersonContactForm(ModelForm):
    class Meta:
        model = PersonContact
        fields = '__all__'

        widgets = {
            'first_name': TextInput(attrs={'class':'gg'}),
            'first_name': TextInput(attrs={'class':'gg'}),
            'phone_number': NumberInput(attrs={'class': 'gg'}),
            'email': EmailInput(attrs={'class': 'gg'}),
            'date_of_birth': DateInput(attrs={'class': 'gg', 'type':'date'})

        }