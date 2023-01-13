from django.shortcuts import render
from  django.http import HttpResponse
from .models import Product,Offer
# Create your views here.
def index(request):
    products=Product.objects.all()
    return render(request,'index.html',{'products':products}) 
    #return HttpResponse("<h1>Hello, Welocome to my app</h1>")
def about(request):
    return HttpResponse("<h1>cool func</h1>")
def support(request):
    return HttpResponse("<h1>Something about us</h1>")