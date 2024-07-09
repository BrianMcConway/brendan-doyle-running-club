from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Div
from django.contrib.auth.models import User
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Field('bio', css_class='form-control'),
                Submit('save', 'Save', css_class='btn btn-primary'),
                css_class='form-group'
            )
        )

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None  # Remove help text for username
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Field('username', css_class='form-control'),
                Field('first_name', css_class='form-control'),
                Field('last_name', css_class='form-control'),
                Field('email', css_class='form-control'),
                Submit('save', 'Save', css_class='btn btn-primary'),
                css_class='form-group'
            )
        )

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['old_password', 'new_password1', 'new_password2']:
            self.fields[field_name].help_text = None
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Field('old_password', css_class='form-control'),
                Field('new_password1', css_class='form-control'),
                Field('new_password2', css_class='form-control'),
                Submit('change_password', 'Change Password', css_class='btn btn-primary'),
                css_class='form-group'
            )
        )
