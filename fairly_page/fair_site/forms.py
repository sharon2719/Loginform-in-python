from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# creation of forms
class NewUserForm(UserCreationForm):
    email=forms.EmailField(required=True)     #user inputs email which is in the correct format

    class Meta:              #tells the parent class what to do
        model=User
        fields=("username","email","password1","password2")
    
    def save (self,commit=True):
        user=super(NewUserForm,self).save(commit=False)
        user.email=self.cleaned_data['email']        #helps to access the validated form
        if commit:
            user.save()
        return user
            
