from django.shortcuts import render
from .models import*

def home(Request):
    data=Product.objects.all().order_by('id').reverse()
    return render(Request,"index.html",{'data':data})

def shop(Request):
    data=Product.objects.all().order_by('id').reverse()
    return render(Request,"shop.html",{'data:data'})
