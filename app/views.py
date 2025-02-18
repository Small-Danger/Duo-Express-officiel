from django.shortcuts import render,redirect


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
def achat_billet(request):
    return render(request,'achat billets/index6.html')
    
    
#def whatsapp_redirect(request, service_id):
#    service = Service.objects.get(id=service_id)
#    return redirect(f"https://wa.me/{service.numero_whatsapp}")