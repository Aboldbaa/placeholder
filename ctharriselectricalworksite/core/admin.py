from django.contrib import admin
from .models import Client, Invoice, Material, InvoiceMaterial
# Register your models here.

admin.site.register(Client)
admin.site.register(Invoice)
admin.site.register(Material)
admin.site.register(InvoiceMaterial)