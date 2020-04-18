from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template import Context, loader
from account.models import Usertype
from masks.models import Order, OrderProduct
from .forms import UserForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    context={}
    if request.user.is_authenticated:
        return redirect('/news1')
    return render(request, 'account/index.html', context)

def login_now(request):
    user = authenticate(username=request.POST.get('login'), password=request.POST.get('password'))
    if user is not None:
        login(request, user)
        return redirect('/account/cabinet')
    else:
        return redirect('/account/')

def edit(request):
    user_info = get_object_or_404(Usertype, user_id=request.user.id)
    userform = UserForm(instance = user_info)
    if userform.is_valid():
        userform.save()
    context={
    "user" : request.user,
    "user_info" : user_info,
    }
    return render(request, 'account/edit.html', context)

@csrf_exempt
def save(request):
    user_info = get_object_or_404(Usertype, user_id=request.user.id)
    user = UserForm(request.POST, instance = user_info)
    context = {}
    if user.is_valid():
        try:
            user.save()
            return HttpResponse("OK")
        except:
            return HttpResponse("Bad")
        return HttpResponse("Valid")
    return HttpResponse("NOT VALID")

def cabinet(request):
    if request.user.is_authenticated:
        user_info = get_object_or_404(Usertype, user_id=request.user.id)
        user_info
        context={
        "user" : request.user,
        "user_info" : user_info,
        }
        return render(request, 'account/cabinet.html', context)
    return redirect('/account')


def registration(request):
    if not request.user.is_authenticated:
        context={}
        return render(request, 'account/registration.html', context)
    else:
        return redirect('/account')
def orders(request):
    if  request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user)
        context = {'orders': orders}
        return render(request,'account/order.html', context)
    return redirect('/account')

def register(request):
    if not request.user.is_authenticated:
        username = request.POST.get('login')
        name = request.POST.get('name')
        password = request.POST.get('password')
        user_type = request.POST.get('type')
        email = request.POST.get('email')
        user = User.objects.create_user(username=username, email=email, password=password, first_name=name)
        newusertype = Usertype(user_id = user.id, user_type=user_type)
        newusertype.save()
        return redirect('/account/')
    else:
        return redirect('/account/')
def logoutme(request):
    if  User.is_authenticated:
        logout(request)
    return redirect('/account')
