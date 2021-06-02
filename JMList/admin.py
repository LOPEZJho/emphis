from django.contrib import admin
from .models import Employee, ValidID, Department, EmployeesHealth, WorkHistory

admin.site.register(Employee)
admin.site.register(ValidID)
admin.site.register(Department)
admin.site.register(EmployeesHealth)
admin.site.register(WorkHistory)

# Register your models here.
