from django.forms import ModelForm, forms
from news.models import News

class ArticleForm(ModelForm):
    class Meta:
        model = News
        fields = ['category', 'news_title', 'short_description', 'text', 'img_url', 'author']
