from django.contrib import admin
from .models import City

class detailsAdmin(admin.ModelAdmin):
    list_display = ('name','temperature','description')
    list_display_links=('name',)


admin.site.register(City, detailsAdmin)