from django.contrib import admin
from .models import Pages

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')
    #change_list_template = "admin/grapesjs.html"
    #add_form_template = "admin/grapesjs.html"

admin.site.register(Pages, PageAdmin)
admin.site.site_header = "Pando Software"
