from django.contrib import admin
from . import models

@admin.register(models.users)
class userAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'first_name','last_name','email','password','contact')

@admin.register(models.expenses)
class expensesAdmin(admin.ModelAdmin):
    list_display = ('bill_id','euser_id', 'title','description','amount','date')

@admin.register(models.split_bill)
class split_billAdmin(admin.ModelAdmin):
    list_display = ('sbill_id','suser_id', 'title','description','amount','split','date')

@admin.register(models.group)
class groupAdmin(admin.ModelAdmin):
    list_display = ('gbill_id', 'guser_id', 'amount')

@admin.register(models.buddy)
class buddyAdmin(admin.ModelAdmin):
    list_display = ('buser_id', 'member_id')
