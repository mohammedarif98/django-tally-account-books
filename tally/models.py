
from django.db import models

# Create your models here.
'''--------- group summary -----------'''
class tally_group(models.Model):
    group_name = models.CharField(max_length=255,null=True)
    group_alias = models.CharField(max_length=255,null=True)
    group_under = models.CharField(max_length=255,null=True)
    nature = models.CharField(max_length=255,null=True)
    gross_profit = models.CharField(max_length=255 ,null=True)
    sub_ledger = models.CharField(max_length=255,null=True)
    debit_credit = models.CharField(max_length=255,null=True)
    calculation = models.CharField(max_length=255,null=True)
    invoice = models.CharField(max_length=255,null=True)


class First_Group_Summary_Model(models.Model):
    Group_Name=models.ForeignKey(tally_group,on_delete=models.CASCADE,null=True)
    Particular=models.CharField(max_length=40,null=True)
    Debit=models.IntegerField(default=0,null=True)
    Credit=models.IntegerField(default=0,null=True)

class Second_Group_Summary_Model(models.Model):
    Fgroup_Forng=models.ForeignKey(First_Group_Summary_Model,on_delete=models.CASCADE)
    CName=models.CharField(max_length=50,null=True)

class Third_Group_Summary_Model(models.Model):
    Sgroup_Forng=models.ForeignKey(Second_Group_Summary_Model,on_delete=models.CASCADE)
    PName=models.CharField(max_length=50,null=True)

class Ledger_Monthly_Summary_Model(models.Model):
    Tgroup_Forgn=models.ForeignKey(Third_Group_Summary_Model,on_delete=models.CASCADE)
    Open_Balance=models.IntegerField(default=0,null=True)
    Particular=models.CharField(max_length=30,null=True)
    Dedit=models.IntegerField(default=0,null=True)
    Credit=models.IntegerField(default=0,null=True)
    Closing_Balance=models.IntegerField(default=0,null=True)

class Ledger_Voucher_Model(models.Model):
    Particular=models.CharField(max_length=30,null=True)
    Date=models.DateField(auto_now_add=True,null=True)
    Vch_Type=models.CharField(max_length=40,null=True)
    Vch_No=models.IntegerField(default=0,null=True)
    Debit=models.IntegerField(default=0,null=True)
    Credit=models.IntegerField(default=0,null=True)
    Open_Balance=models.IntegerField(default=0,null=True)

'''-------------- group voucher -----------------'''

# class Create_Group_Voucher_Model(models.Model):
#     Name=models.CharField(max_length=30,null=True)
#     Alias=models.CharField(max_length=30,null=True)
#     Under=models.CharField(max_length=40,null=True)
#     Group_Subledger=models.CharField(max_length=10,null=True)
#     Nett_DebitCredit_Reporting=models.CharField(max_length=10,null=True)
#     Used_Calculation=models.CharField(max_length=10,null=True)
#     Method_Purchase_Invoice=models.CharField(max_length=30,null=True)

class First_Voucher_Summary_Model(models.Model):
    Voucher_Name=models.ForeignKey(tally_group,on_delete=models.CASCADE)
    Particular=models.CharField(max_length=40,null=True)
    Debit=models.IntegerField(default=0,null=True)
    Credit=models.IntegerField(default=0,null=True)

class Second_Voucher_Summary_Model(models.Model):
    FVoucher_Name=models.ForeignKey(First_Voucher_Summary_Model,on_delete=models.CASCADE)
    Particular=models.CharField(max_length=40,null=True)
    Debit=models.IntegerField(default=0,null=True)
    Credit=models.IntegerField(default=0,null=True)

class Stock_Group_Summary_Model(models.Model):
    Stock_Voucher_Forgn=models.ForeignKey(tally_group,on_delete=models.CASCADE)
    Particular=models.CharField(max_length=40,null=True)
    Quantity=models.IntegerField(default=0,null=True)
    Rate=models.IntegerField(default=0,null=True)
    Value=models.IntegerField(default=0,null=True)


class Product_Stock_Group_Summary_Model(models.Model):
    PStock_Voucher_Forgn=models.ForeignKey(Stock_Group_Summary_Model,on_delete=models.CASCADE,null=True)
    Particular=models.CharField(max_length=40,null=True)
    Quantity=models.CharField(max_length=40,null=True)
    Rate=models.IntegerField(default=0,null=True)
    Value=models.IntegerField(default=0,null=True)

class Stock_Item_Monthly_Summary_Model(models.Model):
    Pro_Stock_Voucher_Forgn=models.ForeignKey(Product_Stock_Group_Summary_Model,on_delete=models.CASCADE,null=True)
    Open_Balance_Qty=models.IntegerField(default=0,null=True)
    Open_Balance_Value=models.IntegerField(default=0,null=True)
    Particular=models.CharField(max_length=50,null=True)
    Inwards_Qty=models.IntegerField(default=0,null=True)
    Inwards_Vlu=models.IntegerField(default=0,null=True)
    Outwards_Qty=models.IntegerField(default=0,null=True)
    Outwards_Vlu=models.IntegerField(default=0,null=True)
    Closing_Bal_Qty=models.IntegerField(default=0,null=True)
    Closing_Bal_Vlu=models.IntegerField(default=0,null=True)

class Stock_Item_Voucher_Model(models.Model):
    Pro_Stock_Forgn=models.ForeignKey(Stock_Item_Monthly_Summary_Model,on_delete=models.CASCADE,null=True)
    Date=models.DateField(auto_now_add=True)
    Particular=models.CharField(max_length=50,null=True)
    Voucher_Type=models.CharField(max_length=40,null=True)
    Vch_No=models.IntegerField(default=0,null=True)
    Inwards_Qty=models.IntegerField(default=0,null=True)
    Inwards_Vlu=models.IntegerField(default=0,null=True)
    Outwards_Qty=models.IntegerField(default=0,null=True)
    Outwards_Vlu=models.IntegerField(default=0,null=True)


class Group_Voucher_Model(models.Model):
    Date=models.DateField(auto_now_add=True,null=True)
    Particular=models.CharField(max_length=40,null=True)
    Vch_Type=models.CharField(max_length=40,null=True)
    Vch_No=models.IntegerField(default=0,null=True)
    DEBIT=models.IntegerField(default=0,null=True)
    Credit=models.IntegerField(default=0,null=True)
    Open_Balance=models.IntegerField(default=0,null=True)




