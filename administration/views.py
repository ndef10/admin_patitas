from django.shortcuts import render
from .models import Provider, Customer, Pet

# Create your views here.
def v_index(request):
    context = {
        "n_providers": 0,
        "n_customers": 0,
        "n_pets": 0
    }

    context["n_providers"] = Provider.objects.all().count()
    context["n_customers"] = Customer.objects.all().count()
    context["n_pets"] = Pet.objects.all().count()

    return render(request, 'administration/index.html', context)

def v_providers(request):
    context = {
        "provs": Provider.objects.all() 
    }
    return render(request, "administration/providers.html", context)
