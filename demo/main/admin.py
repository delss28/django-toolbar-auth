from django.contrib import admin
from .models import Doctor, Service

admin.site.register(Doctor)

@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


