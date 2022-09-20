from tally import views
from django.urls import path

urlpatterns=[
# groupe-summary 
    path('',views.Index,name='Index'),
    path('Group_Summary/<int:pk>',views.Group_Summary,name='Group_Summary'),
    path('Sec_Group_Summary/<int:pk>',views.Sec_Group_Summary,name="Sec_Group_Summary"),
    path('Thrd_Group_Summary/<int:pk>',views.Thrd_Group_Summary,name="Thrd_Group_Summary"),
    path('Ledger_Monthly_Summary/<int:pk>',views.Ledger_Monthly_Summary,name='Ledger_Monthly_Summary'),
    path('Ledger_Voucher/<int:pk>',views.Ledger_Voucher,name='Ledger_Voucher'),
    path('Select_Groups',views.Select_Groups,name='Select_Groups'),
    path('Creat_Group_Summary',views.Creat_Group_Summary,name='Creat_Group_Summary'),
    path('Group_Summary_Create',views.Group_Summary_Create,name='Group_Summary_Create'),

# group-voucher
    path('Stock_Group_Summary/<int:pk>',views.Stock_Group_Summary,name='Stock_Group_Summary'),
    path('Stock_Item_Voucher/<int:pk>',views.Stock_Item_Voucher,name='Stock_Item_Voucher'),
    path('Stock_Item_Monthly_Summary/<int:pk>',views.Stock_Item_Monthly_Summary,name="Stock_Item_Monthly_Summary"),
    path('Group_Voucher/<int:pk>',views.Group_Voucher,name="Group_Voucher"),
    path('Voucher_Group_Summary/<int:pk>',views.Voucher_Group_Summary,name="Voucher_Group_Summary"),
    path('Creat_Group_Voucher',views.Creat_Group_Voucher,name='Creat_Group_Voucher'),
    path('Select_Group_Voucher',views.Select_Group_Voucher,name='Select_Group_Voucher'),
    path('Group_Voucher_Create',views.Group_Voucher_Create,name='Group_Voucher_Create'),
    path('Group_Voucher_Summary/<int:pk>',views.Group_Voucher_Summary,name="Group_Voucher_Summary"),
    path('Stock_Group_Summary_Product/<int:pk>',views.Stock_Group_Summary_Product,name="Stock_Group_Summary_Product"),


]