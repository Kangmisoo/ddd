from django.shortcuts import render, redirect
from . models import Products
# Create your views here.
def product(request) :
    p = Products.objects.all().values()
    return render(request,'p_list.html',{'p':p})
def add(request) :
    return render(request, 'insert.html')
def addrecord(request) :
    name = request.POST['name']
    img = request.POST['img']
    price = request.POST['price']
    p =Products(name=name,img=img,price=int(price))
    p.save()
    return redirect('product')
def delete(request,id) :
    p=Products.objects.get(id=id)
    p.delete()
    return redirect('product')
def update(request,id) :
    p=Products.objects.get(id=id)
    return render(request,'p_update.html', {'p': p })

