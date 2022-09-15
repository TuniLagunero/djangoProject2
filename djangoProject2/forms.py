from django import forms

class ContactForm(forms.Form):
    fullname = forms.Charfield(widget=forms.Textinput(
        attrs={
            "class": "form-control",
            "placeholder": "Fullname"
        }
    ))
    email = forms.EmailField(widget=forms.Emailinput(
        attrs={
            "class": "form-control",
            "placeholder": "email"
        }
    ))
    content = forms.Charfield(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Message"
        }
    ))