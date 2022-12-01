from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    salary_hr = models.IntegerField()
    working_hrs = models.IntegerField()
    total_salary = models.IntegerField(null=True, blank=True)
    