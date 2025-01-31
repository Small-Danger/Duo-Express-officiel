from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request,'index.html')
def transport_aerien(request):
    return render(request,'transport Aerien/index.html')
def transport_bateau(request):
    return render(request,'transport Maritime/index4.html')
def calculatrice(request):
    return render(request,'calculatrice/index.html')
def achat_international(request):
    return render(request,'achat international/index5.html')