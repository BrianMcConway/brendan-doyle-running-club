from django import forms
from .models import Booking
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['race', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Booking'))
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'