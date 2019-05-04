from django import forms

from .models import Pet


class PetCreateForm(forms.ModelForm):

    class Meta:
        model = Pet
        fields = ('name', 'birthday', 'animal', 'registration_number',
                  'diseases_info', 'allergies_info', 'preferences', 'is_main')


class PetChangeForm(forms.ModelForm):

    class Meta:
        model = Pet
        fields = ('name', 'birthday', 'animal', 'registration_number',
                  'diseases_info', 'allergies_info', 'preferences', 'is_main')
        widgets = {
            'birthday': forms.SelectDateWidget(years=range(1900, 2020)),
            'phone': forms.TextInput(attrs={'disabled': True}),
        }
