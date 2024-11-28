from django.contrib import admin
from .models import Provider, Customer, Pet
from django.conf import settings
from django.conf.urls.static import static
from django.utils.html import format_html
# Register your models here.

admin.site.site_header = "Patitas - Dashboard"
admin.site.site_title = "Patitas - Dashboard"
admin.site.index_title = "Patitas - Dashboard"
 
@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('identificador', 'nombres', 'apellidos', )

    @admin.display(description="Apellidos")
    def apellidos(self, obj):
        return obj.last_name
    
    @admin.display(description="Nombres")
    def nombres(self, obj):
        return obj.first_name
    
    @admin.display(description="Identificador")
    def identificador(self, obj):
        if obj.main_photo:
            return format_html('<img src={} style="width: 64px;" /><br />' + str(obj.id), 
                            obj.main_photo.url)
        return obj.id

class PetInline(admin.TabularInline):
    model = Pet
    extra = 1

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display =('identificador', 'nombre', 'apellido', 'direccion', )

    inlines = [PetInline]

    @admin.display(description="Identificador")
    def identificador(self, obj):
        return obj.id

    @admin.display(description="Nombre")
    def nombre(self, obj):
        return obj.first_name

    @admin.display(description="Apellido")
    def apellido(self, obj):
        return obj.last_name
    
    @admin.display(description="Direccion")
    def direccion(self, obj):
        return obj.address
        

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display =('nombre', 'fotografia', )

    @admin.display(description="Nombre")
    def nombre(self, obj):
        return obj.name
    
    @admin.display(description="Fotografia")
    def fotografia(self, obj):
        return format_html('<img src={} style="width: 64px;" /><br />' + str(obj.id), 
                            obj.main_photo.url)
        return obj.id
    