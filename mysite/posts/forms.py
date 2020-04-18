from django.forms import ModelForm, forms
from django.forms.widgets import *
from posts.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'cover', 'category']
        widgets = {'cover': FileInput(attrs={"class":"custom-file-input", "id":"inputGroupFile01", "aria-describedby":"inputGroupFileAddon01"}), 'title': TextInput(attrs={"class":"form-control"})}
