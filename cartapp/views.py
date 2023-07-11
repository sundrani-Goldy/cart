from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
import json
from .models import * 

# Create your views here.


def index(request):
    products = Product.objects.all()  # fetching data from database..

    params = {'products': products}  # passing an template with name product
    return render(request, "index.html", params)


def about(request):
    return render(request, "about.html")



def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemjson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        address=request.POST.get('address', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zipcode=request.POST.get('zipcode', '')
        order = Orders(items_json=items_json, name=name, email=email, phone=phone, address=address, city=city,state=state, zipcode=zipcode)
        order.save()
       
        thank = True
        id = order.order_id
        return render(request, 'checkout.html', {'thank':thank, 'id': id}) #sending parametre thank and id in script
    return render(request, 'checkout.html')