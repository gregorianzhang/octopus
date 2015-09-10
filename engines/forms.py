from django import forms

class AddEngineForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Cpus = forms.IntegerField()
    Memory = forms.IntegerField()
    Addr = forms.CharField(max_length=100)

