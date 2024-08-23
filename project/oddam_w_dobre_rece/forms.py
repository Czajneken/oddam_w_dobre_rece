from django import forms
from phonenumber_field.formfields import PhoneNumberField


class DonationToCharityForm(forms.Form):
    quantity = forms.IntegerField()
    address = forms.CharField(max_length=128)
    phone_number = PhoneNumberField()
    city = forms.CharField(max_length=128)
    zip_code = forms.CharField(max_length=6)
    pick_up_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'RRRR-MM-DD'}))
    pick_up_time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '--:--'}))
    pick_up_comment = forms.CharField(widget=forms.Textarea(attrs={'rows': '5'}), required=False)


class EditUserForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=60)
    email = forms.EmailField()


class EditUserPasswordForm(forms.Form):
    password = forms.PasswordInput()
    password2 = forms.PasswordInput()

