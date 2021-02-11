from django import forms


class PersonDetailsForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'id': 'name',
        'placeholder': 'What is your name?'
    }))
    location = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'id': 'last',
        'placeholder':  'Where are you from?'
    }))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'How old are you?'
    }))


class PrayerDetailsForm(forms.Form):
    prayer = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control mt-6',
        'cols': 10,
        'rows': 10
    }))


# class PaymentDetailsForm(forms.Form):
#     email = forms.CharField(widget=forms.EmailInput(attrs={
#         'class': 'form-control',
#         'id': 'email',
#         'placeholder': 'Your Email'
#     }))
#
#     address = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control mt-4',
#         'placeholder': 'Billing Address',
#         'id': 'address'
#     }))
#
#     phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={
#         'class': 'form-control mt-4 mb-4',
#         'placeholder': 'Phone Number',
#         'id': 'phone'
#     }))


class ScheduledDateForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date',
        'class': 'form-control mt-5'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control mt-4',
        'id': 'email',
        'placeholder': 'Your Email'
    }))
