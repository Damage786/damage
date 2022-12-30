from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=30)
    name = models.CharField(max_length=20,null=True)
    desc = models.CharField(max_length=300,null=True)

    def __str__(self):
        return self.name
    

# class Contact(models.Model):
#     email = models.CharField(max_length=50)
#     name = models.CharField(max_length=50)
#     desc = models.CharField(max_length=50)
