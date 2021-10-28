from django import forms
from django.contrib.auth import get_user_model
# from .models import LeaveMessage

user = get_user_model()


class ContactUsPageForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "نام خود را وارد کنید...",
                   "id": "name", "type": "text"}
        ), max_length=50,
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "name@example.com",
                   "id": "email", "type": "email"}
        ), max_length=60,
    )
    phone_number = forms.CharField(
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "09120001122",
                   "id": "phone", "type": "tel"}
        ), max_length=75,
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "پیام خود را همینجا وارد کنید....", "id": "message",
                   "type": "text", "style": "height: 10rem"}
        )
    )
