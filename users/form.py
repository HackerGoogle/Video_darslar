from django import forms 
from .models import Users,UserProfile
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model=Users
        fields = ["image","first_name","last_name","username","email","password1","password2"]
        widgets={
            'image': forms.FileInput(attrs={'class':'form-control fs-5'}),
            'username': forms.TextInput(attrs={'class':'form-control fs-5'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control fs-5',}),
            'email': forms.TextInput(attrs={'class': 'form-control fs-5',}),
            'password1': forms.TextInput(attrs={'class': 'form-control fs-5',}),
            'password2': forms.TextInput(attrs={'class': 'form-control fs-5'})
            }
        
class LogInForm(UserCreationForm):
    class Meta:
        model=Users
        fields=["username","password"]
        widgets={
            'username': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'password': forms.TextInput(attrs={'class': 'form-control fs-5',}),
            }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['last_name',]  # Last nomini tahrirlash imkoniyatini beramiz