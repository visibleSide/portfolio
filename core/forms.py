from django import forms

class ContactForm(forms.Form):
    name = forms.EmailField(required=True)
    email = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)