from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["content","content2","content3","content4", "created_date"]
    list_display_links = ["content","content2","content3","content4", "created_date"]
    search_fields= ["content","content2","content3","content4", "created_date"]
    list_filter =["created_date"]

    class Meta:
        model = Contact