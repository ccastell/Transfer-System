from django import forms
from models import User

class UserInputForm(forms.ModelForm):
	user_id = forms.CharField(widget = forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)




class user_create_form(forms.ModelForm):
	user_id = forms.CharField(widget = forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
    	model = User
    	field = ('user_id','password')