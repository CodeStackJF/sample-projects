from django import forms
from users.models import User

class UserCreateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):

    class Meta:
            model = User
            fields = ['first_name', 'last_name', 'email', 'phone_number']
            widgets = {
                'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                'email': forms.EmailInput(attrs={'class': 'form-control'}),
                'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            }

    def save(self, commit=True):
            user = super().save(commit=False)
            if commit:
                user.save()
            return user