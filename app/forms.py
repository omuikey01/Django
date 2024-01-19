from django import forms
from .models import StudentModelRegistration

class StudentFormRegistration(forms.ModelForm) :
    class Meta :
        model = StudentModelRegistration
        fields = "__all__"


class LoginForm(forms.Form) :
    Email = forms.EmailField(label='Email ', max_length=200, required=True)
    Password = forms.CharField(label="Password ", max_length=100, required=True)

class StudentQueryForm(forms.Form):
    Query_Email = forms.EmailField(label="Email ", required=True)
    Query_Subject = forms.CharField(label="Subject ", max_length=200, required=True)
    Query = forms.CharField(widget=forms.Textarea, label="Query")