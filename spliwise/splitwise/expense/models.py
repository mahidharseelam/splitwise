from django.db import models

# Create your models here.
class users(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)

class expenses(models.Model):
    bill_id = models.AutoField(primary_key=True)
    euser_id = models.ForeignKey(users,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    amount = models.IntegerField()
    date = models.DateTimeField()

class split_bill(models.Model):
    sbill_id = models.AutoField(primary_key=True)
    suser_id = models.ForeignKey(users, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    amount = models.IntegerField()
    split = models.CharField(max_length=20)
    date = models.DateTimeField()

class group(models.Model):
    gbill_id = models.ForeignKey(split_bill,on_delete=models.CASCADE)
    guser_id = models.ForeignKey(users,on_delete=models.CASCADE)
    amount = models.IntegerField()

class buddy(models.Model):
    buser_id = models.ForeignKey(users, on_delete=models.CASCADE)
    member_id = models.IntegerField()

