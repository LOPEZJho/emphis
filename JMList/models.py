from django.db import models

class List(models.Model):
	pass

class Item(models.Model):
	text = models.TextField(default="")
	last = models.TextField(default="")
	valID = models.TextField(default="")
	valNum = models.TextField(default="")
	date = models.TextField(default="")
	list = models.ForeignKey(List, default=None, on_delete=models.PROTECT)
# Create your models here.
