from django.contrib import admin
from .models import Contact,About
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name','Last_name','city','state','created_at','is_active',)
    list_filter= ('created_at','is_active',)
    list_editable=('is_active',)
admin.site.register(Contact,ContactAdmin)
admin.site.register(About)