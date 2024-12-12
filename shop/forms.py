from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,SetPasswordForm
from django import forms
from django.core.exceptions import ValidationError
from .models import Profile

class UserInfoForm(forms.ModelForm):
    phone=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'شماره تماس'}),required=False)
    address1=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'آدرس اول'}),required=False)
    address2=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'آدرس دوم'}),required=False)
    city=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'شهر'}),required=False)
    state=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'استان'}),required=False)
    zipcode=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'کدپستی'}),required=False)
    country=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'کشور'}),required=False)

    class Meta:
         model= Profile
         fields=('phone','address1','address2','city','state','zipcode','country')


   


class UpdatePasswordForm(SetPasswordForm):
    new_password1=forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                   'class':'form-control',
                   'name':'password',
                   'type':'password',
                   'placeholder':'رمز بالای 8 کارکتر را وارد کنید'

                   }))
    

    new_password2=forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                   'class':'form-control',
                   'name':'password',
                   'type':'password',
                   'placeholder':'دوباره رمز خود را وارد کنید'

                   }))
   




    class Meta:
          model =User
          fields=['new_password1','new_password2']
           
          error_messages={
            'required': ('این فیلد نمی‌تواند خالی باشد.'),
            
        },
    




class UpdateUserForm(UserChangeForm):
    
    password=None


    first_name=forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام خود را وارد کنید'}),required=False
        )

    last_name=forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام خانوادگی را وارد کنید'}),required=False
        )
    
    email=forms.EmailField(
        label="",
        max_length=50,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder':'ایمیل خود را وارد کنید'}),required=False
            )
    
    username=forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder':'نام کاربری'}))
    
  
    class Meta:
         model=User
         fields=['first_name',
                 'last_name',
                 'email',
                 'username',
         ]





class SignupForm(UserCreationForm):


    first_name=forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام خود را وارد کنید'})
        )

    last_name=forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام خانوادگی را وارد کنید'})
        )
    
    email=forms.EmailField(
        label="",
        max_length=50,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder':'ایمیل خود را وارد کنید'})
            )
    
    username=forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder':'نام کاربری'}))
    
    password1=forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                   'class':'form-control',
                   'name':'password',
                   'type':'password',
                   'placeholder':'رمز بالای 8 کارکتر را وارد کنید'

                   }))
    

    password2=forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                   'class':'form-control',
                   'name':'password',
                   'type':'password',
                   'placeholder':'دوباره رمز خود را وارد کنید'

                   }))
    
    class Meta:
         model=User
         fields=['first_name',
                 'last_name',
                 'email',
                 'username',
                 'password1',
                 'password2'
         ]

