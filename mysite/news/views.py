from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from news.models import News, Category
import json
from django.views.decorators.csrf import csrf_exempt
from .forms import ArticleForm
import datetime

def index(request):
    all_news = []
    categories = Category.objects.all()
    for category in categories:
        for new in category.news_set.all():
            all_news.append(new)
    context = {'news': all_news}
    return render(request, 'news/index.html', context)

def addnew(request):
    context = {}
    return render(request, 'news/addnew.html', context)

def articleview(request, pk):
    article = get_object_or_404(News, pk=pk)
    context = {'article':article}
    return render(request, 'news/articleview.html', context)

def editor(request, pk):
    new = get_object_or_404(News, pk=pk)
    context = {'new':new}
    return render(request, 'news/editor.html', context)

@csrf_exempt
def get_article(request):
    article = ArticleForm(request.POST)
    context = {}
    if article.is_valid():
        try:
            article.save()
            return HttpResponse("OK")
        except:
            return HttpResponse("Bad")

    return HttpResponse("NOT VALID")

@csrf_exempt
def edit_article(request, pk):
    has_article = get_object_or_404(News, pk = pk)
    article = ArticleForm(request.POST, instance = has_article)

    context = {}
    if article.is_valid():
        try:
            article.save()
            return HttpResponse("OK")
        except:
            return HttpResponse("Bad")
        return HttpResponse("Valid")
    return HttpResponse("NOT VALID")


@csrf_exempt
def add(request):
    small = request.POST.get('small')
    return HttpResponse("Hi")

# Create your views here.
