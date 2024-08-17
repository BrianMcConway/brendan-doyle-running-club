from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Div
from django.contrib.auth.models import User
from .models import Profile


class UserForm(forms.ModelForm):
    """
    Form for updating User model fields.
    """
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(
                attrs={'autocomplete': 'username'}
            ),
            'first_name': forms.TextInput(
                attrs={'autocomplete': 'given-name'}
            ),
            'last_name': forms.TextInput(
                attrs={'autocomplete': 'family-name'}
            ),
            'email': forms.EmailInput(
                attrs={'autocomplete': 'email'}
            ),
        }

    def __init__(self, *args, **kwargs):
        """
        Initialize the form, remove help text for username,
        and set up crispy forms helper.
        """
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None

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


class ProfileForm(forms.ModelForm):
    """
    Form for updating Profile model fields.
    """
    class Meta:
        model = Profile
        fields = []

    def __init__(self, *args, **kwargs):
        """
        Initialize the form and set up crispy forms helper.
        """
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Submit('save', 'Save', css_class='btn btn-primary'),
                css_class='form-group'
            )
        )


class CustomPasswordChangeForm(PasswordChangeForm):
    """
    Form for changing user passwords.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the form, remove help texts, and set up crispy forms helper.
        """
        super().__init__(*args, **kwargs)

        for field_name in ['old_password', 'new_password1', 'new_password2']:
            self.fields[field_name].help_text = None
            self.fields[field_name].widget.attrs.update(
                {
                    'class': 'form-control',
                    'autocomplete': (
                        'new-password' if 'new' in field_name
                        else 'current-password'
                    )
                }
            )

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Field('old_password', css_class='form-control'),
                Field('new_password1', css_class='form-control'),
                Field('new_password2', css_class='form-control'),
                Submit('change_password', 'Change Password',
                       css_class='btn btn-primary'),
                css_class='form-group'
            )
        )
