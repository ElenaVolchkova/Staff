from django.contrib import admin
from .models import Employee


# @admin.site.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'salary', 'employment_date', 'chief', 'level')
    list_filter = ('position',)
    search_fields = ('name',)


admin.site.register(Employee, EmployeeAdmin)