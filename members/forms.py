from allauth.account.forms import LoginForm, SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Div

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the 'remember' field
        if 'remember' in self.fields:
            del self.fields['remember']
        # Customize the layout using crispy forms
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
        # Override the login method to avoid accessing 'remember' field
        self.cleaned_data['remember'] = False
        return super().login(request, redirect_url)

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove help text
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        # Customize the layout using crispy forms
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
