from django import forms
from .models import User
from django.core.exceptions import ValidationError

class Register_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        uzunligi = len(name)
        harfmi = name.isalpha()

        if uzunligi < 4:
            raise ValidationError('Iltimos yaroqli ism kiriting')

        if harfmi == False:
            raise ValidationError('Ism da son yoki belgi bulishi mumkin emas!')

        return name


    

