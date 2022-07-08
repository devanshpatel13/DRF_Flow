from django.db import models

# Create your models here.


class Home(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    f_name = models.CharField(max_length=100)
    # number1 = models.IntegerField( null= True)

