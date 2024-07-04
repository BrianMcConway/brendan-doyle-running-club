from allauth.account.forms import LoginForm, SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the 'remember' field
        if 'remember' in self.fields:
            del self.fields['remember']
        # Customize the layout if using crispy forms
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'login',
            'password',
            Submit('login', 'Login', css_class='btn btn-primary')
        )

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the help text for all fields
        for field in self.fields.values():
            field.help_text = ''
        # Customize the layout if using crispy forms
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'email',
            'password1',
            'password2',
            Submit('signup', 'Sign Up', css_class='btn btn-primary')
        )
