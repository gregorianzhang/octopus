from django import forms

class AddEngine(form.Form):
    Name = forms.CharField(max_length=30)
    Cpus = forms.IntegerField()
    Memory = forms.IntegerField()
    Addr = forms.CharField(max_length=100)

