from django.contrib import admin
from djangoapp.models import Topics, AccessRecords, WebPage

# Register your models here.
admin.site.register(Topics)
admin.site.register(AccessRecords)
admin.site.register(WebPage)
