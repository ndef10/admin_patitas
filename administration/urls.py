from django.urls import path
from .views import v_index, v_providers

urlpatterns = [
    path('', v_index, name='index'),
    path('providers', v_providers, name= 'providers')
]