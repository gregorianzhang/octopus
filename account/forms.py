from django import forms

class RegisterUserForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=50)
    usertype = forms.IntegerField()


