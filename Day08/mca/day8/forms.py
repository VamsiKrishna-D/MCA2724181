from django.forms import fields  
from .models import studentModel  
from django import forms  
class studentForm(forms.ModelForm):  
    class Meta:  
        model = studentModel  # To specify the model to be used to create form
        fields = '__all__'  # It includes all the fields of model

