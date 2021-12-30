from django import forms
class MyForm(forms.Form):
    Name=forms.CharField(max_length=50)
    Subject=forms.CharField(max_length=50)
    Email=forms.CharField(max_length=50)
    Message=forms.CharField()

