from django import forms
from django.core.exceptions import ValidationError

from .models import Students

class LoginForm(forms.Form):
        username = forms.CharField(label='Username',max_length = 6)
        password = forms.CharField(label='Enter your BINX/ School Password',max_length=10, widget=forms.PasswordInput)
        def clean(self):
                if not str(self.cleaned_data.get('username')).isdigit():
                        raise ValidationError("Invalid Username")
                        return self.cleaned_data
        
                entries  = Students.objects.filter(student_id=self.cleaned_data.get('username'))
                if not entries:
                        raise ValidationError("Incorrect Username")
                        return self.cleaned_data
        
                if entries and entries[0].password != self.cleaned_data.get('password'):
                        raise ValidationError("Incorrect Password")
        
                return self.cleaned_data
