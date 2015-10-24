from django.contrib import admin
from .models import *


# Register your models here.


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'category', 'doc_no', 'was_over_date', 'photo')
    # list_filter = ['was_over_date']
    search_fields = ['full_name']


admin.site.register(Documents, DocumentAdmin)
admin.site.register(Category)
