from django.db import models

# Create your models here.
class Warfile(models.Model):
    Name = models.CharField(max_length=30)
    Comment = models.CharField(max_length=1024)
    Username = models.CharField(max_length=30)

    def __str__(self):
        return self.Name

