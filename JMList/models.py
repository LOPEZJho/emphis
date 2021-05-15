from django.db import models

class Employee(models.Model):
	Name = models.TextField(default="")
	Gender = models.TextField(default="")
	Address = models.TextField(default="")
	Birthday = models.DateField(default="")
	PhoneNumber = models.CharField(default="", max_length=11)
	EmailAddress = models.TextField(default="")
	class meta:
		db_table = "employees"

class ValidID(models.Model):
	EmpID = models.ForeignKey(Employee, default=None, on_delete = models.CASCADE)
	ValID = models.TextField(default="")
	ValNum = models.TextField(default="")
	ValDate = models.DateField(default="")
	class meta:
		db_table = "validid"

class Department(models.Model):
	EmpID = models.ManyToManyField(Employee, default=None)
	DeptName = models.TextField(default="")
	DeptHead = models.TextField(default="")
	class meta:
		db_table = "department"

class EmployeesHealth(models.Model):
	EmpID = models.OneToOneField(Employee, default=None, on_delete = models.CASCADE)
	EHealth = models.TextField(default="")
	Maintenance = models.TextField(default="")
	class meta:
		db_table = "employeeshealth"

class WorkHistory(models.Model):
	Company = models.TextField(default="")
	DeptAssigned = models.TextField(default="")
	Location = models.TextField(default="")
	Contact = models.CharField(default="", max_length=11)
	class meta:
		db_table = "workhistory"

class EmployeesStatus(models.Model):
	PatientId = models.ForeignKey(Employee, default=None, on_delete = models.CASCADE)
	ETestDate = models.DateField(default="")
	EStatus = models.TextField(default="")
	Comments = models.TextField(default="")
	Prescription = models.TextField(default="", max_length = 200)
	Doctor = models.TextField(default="")
	class meta:
		db_table = "employeesstatus"