from django.db import models

class Employee(models.Model):
	name = models.TextField(default="")
	gender = models.TextField(default="")
	address = models.TextField(default="")
	phonenumber = models.CharField(default="", max_length=12)
	emailaddress = models.TextField(default="")
	class meta:
		db_table = "employee"

class ValidID(models.Model):
	employee = models.ForeignKey(Employee, default=None, on_delete = models.CASCADE)
	valid = models.TextField(default="")
	valnum = models.TextField(default="")
	class meta:
		db_table = "validid"

class Department(models.Model):
	employee = models.ManyToManyField(Employee, default=None)
	deptname = models.TextField(default="")
	depthead = models.TextField(default="")
	class meta:
		db_table = "department"

class EmployeesHealth(models.Model):
	employee = models.OneToOneField(Employee, default=None, on_delete = models.CASCADE)
	ehealth = models.TextField(default="")
	maintenance = models.TextField(default="")
	class meta:
		db_table = "employeeshealth"

class WorkHistory(models.Model):
	employee = models.ManyToManyField(Employee, default=None)
	company = models.TextField(default="")
	location = models.TextField(default="")
	contact = models.CharField(default="", max_length=12)
	class meta:
		db_table = "workhistory"