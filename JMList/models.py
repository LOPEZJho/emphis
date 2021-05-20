from django.db import models

class Employee(models.Model):
	Name = models.TextField(default="")
	Gender = models.TextField(default="")
	Address = models.TextField(default="")
	Birthday = models.DateField(default="")
	PhoneNumber = models.CharField(default="", max_length=12)
	EmailAddress = models.EmailField(default="", max_length=75)
	class meta:
		db_table = "employees"

class ValidID(models.Model):
	EmpID = models.ForeignKey(Employee, default=None, on_delete = models.CASCADE)
	ValID = models.TextField(default="")
	ValNum = models.TextField(default="")
	ValDate = models.DateField(default="")
	class meta:
		db_table = "validid"

class WorkHistory(models.Model):
	EmpID = models.ManyToManyField(Employee, default=None)
	Company = models.TextField(default="")
	Location = models.TextField(default="")
	Contact = models.CharField(default="", max_length=12)
	class meta:
		db_table = "workhistory"

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