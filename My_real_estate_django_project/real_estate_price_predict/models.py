from django.db import models

# Create your models here.

class Price(models.Model):
	CRIM=models.FloatField(default=0.0000)
	ZN=models.FloatField(default=0.0000)
	INDUS=models.FloatField(default=0.0000)
	CHAS=models.FloatField(default=0.0000)
	NOX=models.FloatField(default=0.0000)
	RM=models.FloatField(default=0.0000)
	AGE=models.FloatField(default=0.0000)
	DIS=models.FloatField(default=0.0000)
	RAD=models.FloatField(default=0.0000)
	TAX=models.FloatField(default=0.0000)
	PTRATIO=models.FloatField(default=0.0000)
	B=models.FloatField(default=0.0000)
	LSTAT=models.FloatField(default=0.0000)

