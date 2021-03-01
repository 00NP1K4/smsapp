from django import forms
from .models import *
import datetime



class AddContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required')
        for i in Contact.objects.all():
            if i.name == name:
                raise forms.ValidationError(name + ' is already created')
        return name

    def clean_number(self):
        number = self.cleaned_data.get('number')
        if not number:
            raise forms.ValidationError('This field is required')
        for i in Contact.objects.all():
            if i.number == number:
                raise forms.ValidationError(number + ' is already created')
        return number

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"

class ToForm(forms.ModelForm):
    class Meta:
        model = To
        fields = "__all__"

class ContactUpdateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"