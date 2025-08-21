from django.contrib import admin
from.models import Aboutus
# Register your models here.

class AboutusAdmin(admin.ModelAdmin):
    list_display=['title','about']

admin.site.register(Aboutus,AboutusAdmin)
    