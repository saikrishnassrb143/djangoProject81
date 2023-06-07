from django.db import models

class product(models.Model):
    pip=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=20)
    pcost=models.DecimalField(max_digits=20,decimal_places=2)
    pmfdt=models.DateField()
    expdt=models.DateField()
