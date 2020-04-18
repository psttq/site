from django.forms import ModelForm, forms
from account.models import Usertype

class UserForm(ModelForm):
    class Meta:
        model = Usertype
        fields = ['user_photo', 'user_bio']
