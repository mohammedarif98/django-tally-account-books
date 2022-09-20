
from django.shortcuts import render,redirect
from django.db.models import*
from tally.models import*

# from django.http import HttpResponse


# Create your views here.

def Index(request):
    return render(request,'index.html')
    
'''--------- groupe-summary  -----------'''
def Group_Summary(request,pk):
    display=tally_group.objects.get(id=pk)
    data=First_Group_Summary_Model.objects.filter(Group_Name=display)
    sum1=0
    sum2=0
    for i in data:
        sum1+=i.Credit
    for i in data:
        sum2+=i.Debit
    context={'data':data,'display':display,'sum1':sum1,'sum2':sum2}
    return render(request,'acc-book/grp_summary.html',context)

def Sec_Group_Summary(request,pk):
    display=First_Group_Summary_Model.objects.get(id=pk)
    data=Second_Group_Summary_Model.objects.filter(Fgroup_Forng=display)

    sum1=0
    sum2=0
    for i in data:
        sum1+=i.Fgroup_Forng.Credit
    for i in data:
        sum2+=i.Fgroup_Forng.Debit
    context={'data':data,'display':display,'sum1':sum1,'sum2':sum2}

    return render(request,'acc-book/secgrp_sumry.html',context)

def Thrd_Group_Summary(request,pk):
    display=Second_Group_Summary_Model.objects.get(id=pk)
    data=Third_Group_Summary_Model.objects.filter(Sgroup_Forng=display)
    sum1=0
    sum2=0
    for i in data:
        sum1+=i.Sgroup_Forng.Fgroup_Forng.Credit
    for i in data:
        sum2+=i.Sgroup_Forng.Fgroup_Forng.Debit
    context={'data':data,'display':display,'sum1':sum1,'sum2':sum2}
    return render(request,'acc-book/trdgrp_sumry.html',context)

def Ledger_Monthly_Summary(request,pk):
    Display=Third_Group_Summary_Model.objects.get(id=pk)
    data=Ledger_Monthly_Summary_Model.objects.filter(Tgroup_Forgn=Display)
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0

    for a in data:
        sum1 += a.Credit
    for b in data:
        sum2 += b.Dedit
    
    for d in data:
        sum4 += d.Open_Balance

    for c in data:
        sum3 += c.Closing_Balance + sum4

    context={"data":data,'Display':Display,'sum1':sum1,'sum2':sum2,'sum3':sum3,'sum4':sum4}
    return render(request,'acc-book/ledgr_grp_summary.html',context)

def Ledger_Voucher(request,pk):
    display=Ledger_Voucher_Model.objects.all()
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    for a in display:
        sum1+=a.Debit
    for a in display:
        sum2+=a.Credit
    for a in display:
        sum3+=a.Open_Balance
    # for a in display:
    #     sum4+=a.
    sum4=(sum2-sum1)+sum3
    

    context={'display':display,'sum1':sum1,'sum2':sum2,"sum3":sum3,'sum4':sum4}
    return render(request,'acc-book/ledgr_voucher.html',context)

def Select_Groups(request):
    display=tally_group.objects.all()
    context={'display':display}
    return render(request,'acc-book/select_grp.html',context)

def Creat_Group_Summary(request):
    display=tally_group.objects.all()
    context={'display':display}
    return render(request,'acc-book/crt_grp_sumry.html',context)


def Group_Summary_Create(request):
    if request.method=='POST':
        gname=request.POST['gname']
        galias=request.POST['alias']
        under=request.POST['group']
        nature=request.POST['group_nature']
        gross=request.POST['gorss_profit']
        ledg=request.POST['ledger']
        cred=request.POST['debit/credit']
        calc=request.POST['calculation']
        invc=request.POST['invoice']
        grp=tally_group(group_name=gname,
                group_alias=galias,
                group_under=under,
                nature=nature,
                gross_profit=gross,
                sub_ledger=ledg,
                debit_credit=cred,
                calculation=calc,
                invoice=invc,
                )          
        grp.save()
        return redirect('Select_Groups')



'''-------- group-voucher -----------------'''

def Group_Voucher_Summary(request,pk):
    display=tally_group.objects.get(id=pk)
    data=First_Voucher_Summary_Model.objects.filter(Voucher_Name=display)
    sum1=0
    sum2=0
    for i in data:
        sum1+=i.Credit
    for i in data:
        sum2+=i.Debit
    context={'data':data,'display':display,'sum1':sum1,'sum2':sum2}
    return render(request,'acc-book/grp_summary2.html',context)


def Stock_Group_Summary(request,pk):
    display=tally_group.objects.all()
    data=Stock_Group_Summary_Model.objects.filter(id=pk)
    total=0
    for i in data:
        total+=i.Value
    context={"data":data,'display':display,'total':total}
    return render(request,'acc-book/stock_grp_summary.html',context)

def Stock_Group_Summary_Product(request,pk):
    display=Stock_Group_Summary_Model.objects.get(id=pk)
    data=Product_Stock_Group_Summary_Model.objects.filter(PStock_Voucher_Forgn=display)
    total=0
    for i in data:
        total+=i.Value
    context={"data":data,'display':display,'total':total}
    return render(request,'acc-book/stock_grp_summary2.html',context)
    

def Stock_Item_Voucher(request,pk):
    display=Stock_Item_Monthly_Summary_Model.objects.get(id=pk)
    data=Stock_Item_Voucher_Model.objects.filter(Pro_Stock_Forgn=display)
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    sum5=0
    sum6=0
    for i in data:
        sum1+=i.Inwards_Qty
    for i in data:
        sum2+=i.Inwards_Vlu
    for i in data:
        sum3+=i.Outwards_Qty
    for i in data:
        sum4+=i.Outwards_Vlu
    for i in data:
        sum5+=i.Pro_Stock_Forgn.Closing_Bal_Qty
    for i in data:
        sum6+=i.Pro_Stock_Forgn.Closing_Bal_Vlu 
    context={"data":data,'display':display,'sum1':sum1,'sum2':sum2,'sum3':sum3,'sum4':sum4,'sum5':sum5,'sum6':sum6}
    return render(request,'acc-book/stock_item_voucher.html',context)

def Stock_Item_Monthly_Summary(request,pk):
    display=Product_Stock_Group_Summary_Model.objects.get(id=pk)
    data=Stock_Item_Monthly_Summary_Model.objects.filter(Pro_Stock_Voucher_Forgn=display)
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    sum5=0
    sum6=0
    sum7=0
    sum8=0
    for i in data:
        sum1+=i.Open_Balance_Qty
    for i in data:
        sum2+=i.Open_Balance_Value
    for i in data:
        sum3+=i.Inwards_Qty
    for i in data:
        sum4+=i.Inwards_Vlu
    for i in data:
        sum5+=i.Outwards_Qty
    for i in data:
        sum6+=i.Outwards_Vlu
    for i in data:
        sum7+=i.Closing_Bal_Qty
    for i in data:
        sum8+=i.Closing_Bal_Vlu
    context={"data":data,'display':display,'sum1':sum1,'sum2':sum2,'sum3':sum3,'sum4':sum4,'sum5':sum5,'sum6':sum6,'sum7':sum7,'sum8':sum8}
    return render(request,'acc-book/stk_itm_mntly_sumry.html',context)

def Group_Voucher(request,pk):
    display=Group_Voucher_Model.objects.filter(id=pk)
    sum1=0
    sum2=0
    sum3=0
    for i in display:
        sum1+=i.DEBIT
    for i in display:
        sum2+=i.Credit   
    for i in display:
        sum3+=i.Open_Balance
    sum4=(sum1-sum2)-sum3
    context={'display':display,'sum1':sum1,'sum2':sum2,'sum3':sum3,'sum4':sum4}
    return render(request,'acc-book/grp_voucher.html',context)

def Voucher_Group_Summary(request,pk):
    display=First_Voucher_Summary_Model.objects.get(id=pk)
    data=Second_Voucher_Summary_Model.objects.filter(FVoucher_Name=display)
    sum1=0
    sum2=0
    for i in data:
        sum1+=i.Credit
    for i in data:
        sum2+=i.Debit
    context={'data':data,'display':display,'sum1':sum1,'sum2':sum2}
    return render(request,'acc-book/vchr_grp_summary.html',context)

def Creat_Group_Voucher(request):
    display=tally_group.objects.all()
    context={'display':display}
    return render(request,'acc-book/crt_grp_voucher.html',context)

def Select_Group_Voucher(request):
    display=tally_group.objects.all()
    context={'display':display}
    return render(request,'acc-book/select_grp_vchr.html',context)


def Group_Voucher_Create(request):
    if request.method =='POST':
        gname=request.POST['gname']
        galias=request.POST['alias']
        under=request.POST['group']
        nature=request.POST['group_nature']
        gross=request.POST['gorss_profit']
        ledg=request.POST['ledger']
        cred=request.POST['debit/credit']
        calc=request.POST['calculation']
        invc=request.POST['invoice']

        grp=tally_group(group_name=gname,
            group_alias=galias,
            group_under=under,
            nature=nature,
            gross_profit=gross,
            sub_ledger=ledg,
            debit_credit=cred,
            calculation=calc,
            invoice=invc,
            )          
        grp.save()
        return redirect("Select_Group_Voucher")


 