from django.db import models

# Create your models here.
class Engines(models.Model):
    Name = models.CharField(max_length=30)
    Cpus = models.IntegerField()
    Memory = models.IntegerField()
    Addr = models.CharField(max_length=100, primary_key=True)


    def __str__(self):
        return self.Addr

