from django import forms

from .models import Contacts

class PostForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ('name', 'emailAdr', 'phoneNum')