from django import forms
from allauth.account.forms import LoginForm, SignupForm, SetPasswordForm
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError
from .models import GPXFile


class CustomSignupForm(SignupForm):
    """
    Custom signup form to modify password help text and validate username.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    def clean_username(self):
        """
        Validate username to ensure it is not an email address.
        """
        username = self.cleaned_data.get('username')
        if '@' in username and '.' in username:
            raise ValidationError("Username cannot be an email address.")
        return username


class CustomLoginForm(LoginForm):
    """
    Custom login form to remove the 'remember' field.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'remember' in self.fields:
            del self.fields['remember']

    def login(self, request, redirect_url=None):
        """
        Override login method to set 'remember' to False.
        """
        self.cleaned_data['remember'] = False
        return super().login(request, redirect_url)


class CustomSetPasswordForm(SetPasswordForm):
    """
    Custom set password form.
    """
    pass


class CustomPasswordChangeForm(PasswordChangeForm):
    """
    Custom password change form.
    """
    pass


class GPXFileForm(forms.ModelForm):
    """
    Form for uploading GPX files with a title and file field.
    """
    file = forms.FileField(required=True)

    class Meta:
        model = GPXFile
        fields = ['title', 'file']

    def save(self, commit=True, user=None):
        """
        Save the form instance, attaching the file data and optional user.
        """
        instance = super().save(commit=False)
        instance.file_data = self.cleaned_data['file'].read()
        if user:
            instance.uploaded_by = user
        if commit:
            instance.save()
        return instance
