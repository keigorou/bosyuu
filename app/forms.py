from django import forms
from django.db.models import fields
from django.forms import widgets

from .models import User

class UserForm(forms.ModelForm):
    
    class Meta():
        model = User
        
        fields = ('user_store', 'user_name','user_age', 'user_gender', 'user_email', 'user_tel')

        labels = {
            'user_name':'名前',
            'user_age':'年齢',
            'user_gender':'性別',
            'user_email':'メールアドレス',
            'user_tel':'電話番号'
        }

        
  