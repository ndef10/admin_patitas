from django.urls import path
from .views import v_index, v_providers, v_customers, v_pets

urlpatterns = [
    path('', v_index, name='index'),
    path('providers', v_providers, name= 'providers'),
    path('customers', v_customers, name= 'costumers'),
    path('pets',v_pets, name = 'pets')
]