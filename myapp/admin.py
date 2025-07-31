from django.contrib import admin
from myapp.models import Contact, Profile


# Register your models here.
admin.site.site_header = "ZoonCafe | Admin"

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'added_on', 'is_approved']

admin.site.register(Contact, ContactAdmin)
admin.site.register(Profile)
