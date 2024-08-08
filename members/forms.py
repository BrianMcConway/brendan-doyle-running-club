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
    file = forms.FileField(required=True)

    class Meta:
        model = GPXFile
        fields = ['title', 'file']

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        instance.file_data = self.cleaned_data['file'].read()
        if user:
            instance.uploaded_by = user
        if commit:
            instance.save()
        return instance
