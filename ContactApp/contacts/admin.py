from django.contrib import admin
from .models import Contact
# Register your models here.


admin.site.register(Contact)

admin.site.site_header = 'Contact App'
admin.site.site_title = 'Contact App'
