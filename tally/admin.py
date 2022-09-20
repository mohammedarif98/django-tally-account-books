from django.contrib import admin
from tally.models import *

# Register your models here.
@admin.register(First_Group_Summary_Model)
class FirstGroupSummary_Admin(admin.ModelAdmin):
    list_display = ('id','Group_Name','Particular','Debit','Credit')

@admin.register(Second_Group_Summary_Model)
class SecondGroupSummary_Admin(admin.ModelAdmin):
    list_display=('id','Fgroup_Forng','CName')

@admin.register(Third_Group_Summary_Model)
class ThirdGroupSummary_Admin(admin.ModelAdmin):
    list_display=('id','Sgroup_Forng','PName')

@admin.register(Ledger_Monthly_Summary_Model)
class LedgerMonthlySummary_Admin(admin.ModelAdmin):
    list_display=('id','Tgroup_Forgn','Open_Balance','Particular','Dedit','Credit','Closing_Balance')

@admin.register(Ledger_Voucher_Model)
class LedgerVoucher_Admin(admin.ModelAdmin):
    list_display=('id','Particular','Date','Vch_Type','Vch_No','Debit','Credit','Open_Balance')

'''----------voucher summary ----------'''

@admin.register(First_Voucher_Summary_Model)
class FirstVoucherSummary_Admin(admin.ModelAdmin):
    list_display = ('id','Voucher_Name','Particular','Debit','Credit')

@admin.register(Second_Voucher_Summary_Model)
class SecondVoucherSummary_Admin(admin.ModelAdmin):
    list_display = ('id','FVoucher_Name','Particular','Debit','Credit')

@admin.register(Stock_Group_Summary_Model)
class StockVoucherSummary_Admin(admin.ModelAdmin):
    list_display = ('id','Stock_Voucher_Forgn','Particular','Quantity','Rate','Value')

@admin.register(Product_Stock_Group_Summary_Model)
class ProVoucherSummary_Admin(admin.ModelAdmin):
    list_display=('id','PStock_Voucher_Forgn','Particular','Quantity','Rate','Value')

@admin.register(Stock_Item_Monthly_Summary_Model)
class StockItemMontlySummary_Admin(admin.ModelAdmin):
    list_display=('id','Pro_Stock_Voucher_Forgn','Open_Balance_Qty','Open_Balance_Value','Particular','Inwards_Qty',"Inwards_Vlu",'Outwards_Qty','Outwards_Vlu','Closing_Bal_Qty','Closing_Bal_Vlu')

@admin.register(Stock_Item_Voucher_Model)
class Stock_Item_Voucher_Admin(admin.ModelAdmin):
    list_display=('id','Pro_Stock_Forgn','Date','Particular','Voucher_Type','Vch_No','Inwards_Qty','Inwards_Vlu','Outwards_Qty','Outwards_Vlu')

@admin.register(Group_Voucher_Model)
class GroupVoucher_Admin(admin.ModelAdmin):
    list_display=('id','Date','Particular','Vch_Type','Vch_No',"DEBIT",'Credit','Open_Balance')

# admin.site.register(Create_Group_Voucher_Model)

admin.site.register(tally_group)

'''---------------------------------'''



