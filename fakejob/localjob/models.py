from django.db import models

# Create your models here.
class bhubaneswarjob(models.Model):
    date=models.DateTimeField()
    company=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    eligibility=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.IntegerField()


