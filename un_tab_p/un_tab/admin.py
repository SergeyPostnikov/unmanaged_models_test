from django.contrib import admin

from .models import UnmanagedTable

@admin.register(UnmanagedTable)
class UnmanagedTableAdmin(admin.ModelAdmin):
	pass
