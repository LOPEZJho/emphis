from django.contrib import admin
from .models import Employee, ValidID, WorkHistory, Department, EmployeesHealth

admin.site.register(Employee)
admin.site.register(ValidID)
admin.site.register(WorkHistory)
admin.site.register(Department)
admin.site.register(EmployeesHealth)


# Register your models here.
