from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUsuario

class CustomUsuarioForm(UserCreationForm):

    password1 = forms.CharField(label='Password1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password2', widget=forms.PasswordInput)

    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'email')

    def Clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('As senhas não estão iguais')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
