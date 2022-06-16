from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'size': '80'}))
