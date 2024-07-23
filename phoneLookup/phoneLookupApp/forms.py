from django import forms
from phonenumber_field.formfields import PhoneNumberField

class PhoneNumberForm(forms.Form):
    phone_number = PhoneNumberField(region="US")