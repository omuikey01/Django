from django.db import models

# Create your models here.

class StudentModelRegistration(models.Model) :
    Name = models.CharField(max_length=200)
    Phone = models.IntegerField()
    Email = models.EmailField(max_length=254)
    Password = models.CharField(max_length=100)
    Confirm_Password = models.CharField(max_length=100, null=True)
    
class StudentQuery(models.Model):
    Query_Email = models.EmailField(max_length=254)
    Query_Sub = models.CharField(max_length=300)
    QueryDate = models.DateTimeField()
    Query_Query = models.CharField(max_length=1000)