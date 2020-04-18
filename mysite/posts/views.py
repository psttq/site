from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from .models import Post, Category
from .forms import PostForm

def index(request):
    images = Post.objects.all()
    categories = Category.objects.all()
    context = {'images': images, 'categories': categories}
    return render(request, 'posts/index.html', context)

@csrf_exempt
def add(request):
    form = PostForm()
    categories = Category.objects.all()
    context = {'form' : form}
    return render(request, 'posts/add.html', context)

@csrf_exempt
def add_image(request):
    img_post = PostForm(request.POST, request.FILES)
    context = {}
    if img_post.is_valid():
        try:
            img_post.save()
            return redirect('/gallery/')
        except:
            return HttpResponse("Bad")
    return HttpResponse("not valid")
# Create your views here.
