from django import forms
from allauth.account.forms import LoginForm, SignupForm, SetPasswordForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import GPXFile

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'remember' in self.fields:
            del self.fields['remember']

    def login(self, request, redirect_url=None):
        self.cleaned_data['remember'] = False
        return super().login(request, redirect_url)

class CustomSetPasswordForm(SetPasswordForm):
    pass

class CustomPasswordChangeForm(PasswordChangeForm):
    pass

class GPXFileForm(forms.ModelForm):
    file = forms.FileField(required=True)  # Add file field manually

    class Meta:
        model = GPXFile
        fields = ['title']  # Exclude file field from model fields

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            return file.read()
        return None