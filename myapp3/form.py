from django import forms

class CreateContactForm(forms.Form):
	name = forms.CharField(label='name')
	address = forms.CharField(label='address')
	profession = forms.CharField(label='profession')
	telnumber = forms.CharField(label='telnumber')