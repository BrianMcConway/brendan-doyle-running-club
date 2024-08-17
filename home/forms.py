from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ContactForm(forms.Form):
    """
    ContactForm class that defines a form for user contact information.
    Inherits from the forms.Form base class.
    """

    name = forms.CharField(
        max_length=100,
        label='Your Name',
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'name',
                'class': 'form-control'
            }
        )
    )
    email = forms.EmailField(
        label='Your Email',
        widget=forms.EmailInput(
            attrs={
                'autocomplete': 'email',
                'class': 'form-control'
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'autocomplete': 'off',
                'class': 'form-control'
            }
        ),
        label='Your Message'
    )

    def __init__(self, *args, **kwargs):
        """
        Initialize the ContactForm and set up crispy-forms FormHelper.
        """
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Send Message'))
