from django.db import models

# Create your models here.

class Tenant(models.Model):
	tenant_first = models.CharField(max_length=500)
	tenant_last = models.CharField(max_length=500)

	def __str__(self):
		return '{} {}'.format(self.tenant_first, self.tenant_last)

class Landlord(models.Model):
	landlord_first = models.CharField(max_length=500)
	landlord_last = models.CharField(max_length=500)

	def __str__(self):
		return '{} {}'.format(self.landlord_first, self.landlord_last)