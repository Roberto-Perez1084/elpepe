from django.shortcuts import render,redirect
from .models import Producto

# Create your views here.

def index_view(request):
    productos=Producto.objects.all()
    return render(request,'manageProd.html',{'prod':productos})