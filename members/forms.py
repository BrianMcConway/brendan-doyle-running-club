from django import forms
from allauth.account.forms import LoginForm, SignupForm, SetPasswordForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Div

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'remember' in self.fields:
            del self.fields['remember']
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Field('login', css_class='form-control'),
                Field('password', css_class='form-control'),
                Submit('login', 'Login', css_class='btn btn-primary'),
                css_class='form-group'
            )
        )

    def login(self, request, redirect_url=None):
        self.cleaned_data['remember'] = False
        return super().login(request, redirect_url)

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Field('username', css_class='form-control'),
                Field('email', css_class='form-control'),
                Field('password1', css_class='form-control'),
                Field('password2', css_class='form-control'),
                Submit('signup', 'Sign Up', css_class='btn btn-primary'),
                css_class='form-group'
            )
        )

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password2 = forms.CharField(
        label="Confirm new password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Field('new_password1', css_class='form-control'),
                Field('new_password2', css_class='form-control'),
                Submit('set_password', 'Set Password', css_class='btn btn-primary'),
                css_class='form-group'
            )
        )
