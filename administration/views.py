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
        "providers_list": Provider.objects.all() 
    }

    # Obtenemos el valor del query sort_by
    # Si no dan un valor, por defecto se usa "-"
    f_sort_by = request.GET.get("sort_by", "-")
    if f_sort_by == "-": # Si sort_by es -, no hago nada
        pass
    else:
        if f_sort_by == "first_name": # Si sort_by es first_name
            context["providers_list"] = Provider.objects.all().order_by("first_name")
        elif f_sort_by == "last_name":
            context["providers_list"] = Provider.objects.all().order_by("last_name")
            
    
    return render(request, "administration/providers.html", context)

def v_customers(request):
    context = {
        "customers_list": Customer.objects.all() 
    }
    return render(request, "administration/customers.html", context)

def v_pets(request):
    context = {
        "pets_list": Pet.objects.all()
    }
    return render(request, "administration/pets.html", context)