from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    income = models.FloatField(default=0)
    expense = models.FloatField(default=0)
    balance = models.FloatField(default=0)


    def __str__(self):
        return self.user.username



class Transaction(models.Model):
    TYPE = {
        ('Positive','Positive'),
        ('Negative','Negative'),
    }
    profile  = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    transaction_name = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    transaction_type = models.CharField(max_length=50,choices=TYPE)
    created_at = models.DateTimeField(auto_now_add=now)

    def __str__(self):
        return self.transaction_name
