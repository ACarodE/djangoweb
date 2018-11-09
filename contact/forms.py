from django import forms
from .models import Contact

class ContactMessage(forms. ModelForm):
    class Meta:
        model = Contact
        fields = ["content","content2","content3","content4"]