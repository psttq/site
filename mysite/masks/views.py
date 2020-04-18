# -*- coding: utf-8 -*-
import json, random
from django.shortcuts import get_object_or_404, render
from masks.models import Product, Category, Order, OrderProduct, State
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


def index(request):
    context = {}
    return render(request, 'masks/index.html', context)
def contacts(request):
    context = {}
    return render(request, 'masks/contacts.html', context)
def news(request):
    context = {}
    return render(request, 'masks/indev.html', context)
def study(request):
    context = {}
    return render(request, 'masks/indev.html', context)
def courses(request):
    context = {}
    return render(request, 'masks/indev.html', context)
def buy(request):
    categories = Category.objects.all()
    context = {'categories' : categories}
    return render(request, 'masks/buy1.html', context)
def orders(request):
    context = {
        'orders' : Order.objects.order_by('completed'),
    }
    return render(request, 'masks/orders.html', context)
def cart(request):
    if 'cart' in request.session:
        cart = request.session['cart']
        mycart = json.loads(cart)
        for j in range(len(mycart)):
            if mycart[j]['product_id'] is None or mycart[j]['quantity'] is None:
                del mycart[j]
                break
        for i in range(len(mycart)):
            product_id = mycart[i]['product_id']
            product = get_object_or_404(Product, pk=product_id)
            mycart[i]['product'] = product
        context = {
            'data': mycart
        }
        return render(request, 'masks/cart1.html', context)
    else:
        context = {}
        return render(request, 'masks/cart1.html', context)
@csrf_exempt
def order(request):
    name = request.POST.get('name')
    second_name = request.POST.get('second_name')
    mail = request.POST.get('mail')
    number = request.POST.get('number')
    comment = request.POST.get('comment')
    cart = request.session['cart']
    state = get_object_or_404(State, pk=1)
    mycart = json.loads(cart)
    start = "НОВЫЙ ЗАКАЗ: \nИмя: "+ name +" "+ second_name +" \nПочта: "+ mail +" \nНомер: "+ number +" \nКомментарий покупателя: "+ comment +"\nТовары: \n"
    all_sum = 0
    newOrderId = random.randint(0, 999999)
    order = Order(order_id=newOrderId, name=name, surname=second_name, email=mail, number=number, state=state, user=request.user)
    order.save()
    for j in range(len(mycart)):
        if mycart[j]['product_id'] is None or mycart[j]['quantity'] is None:
            del mycart[j]
            break
    temp = 0
    newOrderId = random.randint(0, 999999)
    for i in range(len(mycart)):
        product_id = mycart[i]['product_id']
        product = get_object_or_404(Product, pk=product_id)
        quantity = mycart[i]['quantity']
        orderProduct = OrderProduct(order=order, product=product, quantity=quantity)
        orderProduct.save()
        sum = product.price * int(quantity)
        all_sum += sum
        temp = int(quantity)
        start += product.product_name + "   Кол-во: " + quantity + "    " + str(sum) + "р. \n"
    start += "Итого: " + str(all_sum)
    send_mail('Новый заказ', start, "fmrmedgroup@gmail.com", ['fmrmedgroup@gmail.com'], fail_silently=False)
    return HttpResponse(start)
@csrf_exempt
def sendtext(request):
    name = request.POST.get('name')
    second_name = request.POST.get('second_name')
    mail = request.POST.get('mail')
    number = request.POST.get('number')
    comment = request.POST.get('comment')
    start = "Сообщение: \nИмя: "+ name +" "+ second_name +" \nПочта: "+ mail +" \nНомер: "+ number +" \nКомментарий покупателя: "+ comment +"\n"
    send_mail('Сообщение', start, "fmrmedgroup@gmail.com", ['fmrmedgroup@gmail.com'], fail_silently=False)
    return HttpResponse(start)
@csrf_exempt
def get(request):
    category_id = request.POST.get('category_id')
    category = get_object_or_404(Category, pk=category_id)
    products = category.product_set.all().values()
    return HttpResponse(json.dumps(list(products)), content_type="application/json")
@csrf_exempt
def add(request):
    quantity = request.POST.get('quantity')
    product_id = request.POST.get('product_id')
    if 'cart' in request.session:
        cart = request.session['cart']
        mycart = json.loads(cart)
        flag = False
        for i in range(len(mycart)):
            if mycart[i]['product_id'] == product_id:
                flag = True
                mycart[i]['quantity'] = quantity
        if not flag:
            newProduct = {'product_id':product_id, 'quantity': quantity}
            mycart.append(newProduct)
        newCart = json.dumps(list(mycart))
        request.session['cart'] = newCart
        return HttpResponse(newCart)
    else:
        cart = [{'quantity': quantity, 'product_id': product_id}]
        request.session['cart']=json.dumps(list(cart))
        return HttpResponse("no cart")
@csrf_exempt
def remove(request):
    quantity = request.POST.get('quantity')
    product_id = request.POST.get('product_id')
    if 'cart' in request.session:
        cart = request.session['cart']
        mycart = json.loads(cart)
        flag = False
        for i in range(len(mycart)):
            if mycart[i]['product_id'] == product_id:
                del mycart[i]
                break
        newCart = json.dumps(list(mycart))
        request.session['cart'] = newCart
        return HttpResponse(newCart)
