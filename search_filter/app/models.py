from django.db import models

# Create your models here.
class EmpModel(models.Model):
    emp_name=models.CharField(max_length=75)
    gender=models.CharField(max_length=6)
    occupation=models.CharField(max_length=25)
    salary=models.IntegerField()

    class Meta:
        db_table='employee'