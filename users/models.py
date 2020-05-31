from django.db import models

# Create your models here.


class StudentData(models.Model):

	Full_Name = models.CharField(max_length=200)
	Email_Address = models.EmailField(max_length = 254)
	Contact_Number = models.CharField(max_length=17)
	Roll_Number = models.CharField(max_length=15)
	Department = models.CharField(max_length=200)
	University = models.CharField(max_length=200)

	def __str__(self):
		return self.Full_Name


