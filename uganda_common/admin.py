from django.contrib import admin
from uganda_common.forms import AccessForm
from uganda_common.models import Access

__author__ = 'kenneth'


class AccessAdmin(admin.ModelAdmin):
    form = AccessForm

admin.site.register(Access, AccessAdmin)
