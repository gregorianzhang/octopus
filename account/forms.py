from django import forms

class RegisterUserForm(forms.Form):
    username = forms.CharField(max_length=30)
    #password = forms.CharField(max_length=50)
    #password = forms.PasswordInput()
    password = forms.CharField(widget=forms.PasswordInput)
    usertype = forms.IntegerField()

class LoginUserForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)


