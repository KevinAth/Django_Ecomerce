from django.contrib import admin
from .models import Categoria,productos
# Register your models here.

admin.site.register(Categoria)
@admin.register(productos)
class prodAdmin(admin.ModelAdmin):
    list_display = ("nombre","precio","categoria")
    