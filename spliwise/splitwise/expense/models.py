from django.db import models

# Create your models here.
class users(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    #def __init__(self):
    #    return self.user_id+' '+self.first_name+' '+self.last_name+' '+self.email+' '+self.password+' '+self.contact

class expenses(models.Model):
    bill_id = models.AutoField(primary_key=True)
    euser_id = models.ForeignKey(users,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    amount = models.IntegerField()
    date = models.DateTimeField()
    #def __init__(self):
    #    return self.bill_id,self.euser_id,self.title,self.description,self.amount,self.date

class split_bill(models.Model):
    sbill_id = models.AutoField(primary_key=True)
    suser_id = models.ForeignKey(users, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    amount = models.IntegerField()
    split = models.CharField(max_length=20)
    date = models.DateTimeField()
    #def __init__(self):
    #    return self.sbill_id,self.suser_id,self.title,self.description,self.amount,self.split,self.date

class group(models.Model):
    gbill_id = models.ForeignKey(split_bill,on_delete=models.CASCADE)
    guser_id = models.ForeignKey(users,on_delete=models.CASCADE)
    amount = models.IntegerField()
    #def __init__(self):
    #    return self.gbill_id,self.guser_id,self.amount

class buddy(models.Model):
    buser_id = models.ForeignKey(users, on_delete=models.CASCADE)
    member_id = models.IntegerField()
    #def __init__(self):
    #    return self.buser_id,self.member_id

