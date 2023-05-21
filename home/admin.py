from django.contrib import admin
from .models import sbentry
from import_export.admin import ImportExportModelAdmin

class sbentryAdmin(ImportExportModelAdmin):
    pass

admin.site.register(sbentry, sbentryAdmin)