from django import forms

class SignInForm(forms.Form):
	name = forms.CharField(max_length=20,
		widget=forms.TextInput(attrs={'class' : 'textbox', 'placeholder' : 'Name'}))

