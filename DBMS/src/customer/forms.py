from django import forms               # fill in custom user info then save it 
from .models import customer

class MyRegistrationForm(forms.ModelForm):
    password2= forms.CharField(label="confirm password",widget=forms.PasswordInput)
    class Meta:
        model = customer
        widgets = {
        'password': forms.PasswordInput(),
        }
        fields = [
            'cid',
            'username',
            'email',
            'cname',
            'phone_number',
            'address',
            'password'
        ] 

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = customer.object.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("username is taken") 
        return username  

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2') 
        if password2 != password:
            raise forms.ValidationError("passwords must match.")
        return data  

class  loginForm(forms.ModelForm):
    class Meta:
        model = customer
        widgets = {
        'password': forms.PasswordInput(),
        }
        fields = [
        'username',
        'password'
        ]


            
        