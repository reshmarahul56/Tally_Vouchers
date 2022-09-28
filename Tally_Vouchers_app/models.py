from django.db import models

class Companies(models.Model):
    d_path=models.CharField(max_length=100,null=True)
    name = models.CharField(max_length=255)
    mailing_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10,null=True)
    telephone = models.CharField(max_length=20,null=True)
    mobile = models.CharField(max_length=15,null=True)
    fax = models.CharField(max_length=15,null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=240, null=True)
    website = models.CharField(max_length=100,null=True)
    currency_symbol = models.CharField(max_length=20)
    formal_name = models.CharField(max_length=20)
    fin_begin = models.DateField()
    books_begin = models.DateField()
    fin_end = models.DateField()
    status=models.BooleanField(default=True)


class tally_group(models.Model):
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)
    group_name = models.CharField(max_length=255)
    group_alias = models.CharField(max_length=255)
    group_under = models.CharField(max_length=255)
    nature = models.CharField(max_length=255,null=True)
    gross_profit = models.CharField(max_length=255 ,null=True)
    sub_ledger = models.CharField(max_length=255)
    debit_credit = models.CharField(max_length=255)
    calculation = models.CharField(max_length=255)
    invoice = models.CharField(max_length=255)

class tally_ledger(models.Model):
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255,null=True)
    under = models.CharField(max_length=255)
    grp = models.ForeignKey(tally_group,on_delete = models.CASCADE,null = True)
    mname = models.CharField(max_length=255,null=True)
    address = models.CharField(max_length=255,null=True)
    state = models.CharField(max_length=255,null=True)
    country = models.CharField(max_length=255,null=True)
    pincode = models.CharField(max_length=6,null=True)
    bank_details = models.CharField(max_length=20,null=True)
    pan_no = models.CharField(max_length=100,null=True)
    registration_type = models.CharField(max_length=100,null=True)
    gst_uin = models.CharField(max_length=100,null=True)
    set_alter_gstdetails = models.CharField(max_length=100,null=True)
    opening_blnc = models.IntegerField(null=True)

    set_odl = models.CharField(max_length=255,null=True)
    ac_holder_nm = models.CharField(max_length=255,null=True)
    acc_no = models.CharField(max_length=255,null=True)
    ifsc_code = models.CharField(max_length=255,null=True)
    swift_code = models.CharField(max_length=255,null=True)
    bank_name = models.CharField(max_length=255,null=True)
    branch = models.CharField(max_length=255,null=True)
    SA_cheque_bk = models.CharField(max_length=20,null=True)
    Echeque_p = models.CharField(max_length=20,null=True)
    SA_chequeP_con = models.CharField(max_length=20,null=True)
    
    type_of_ledger = models.CharField(max_length=100,null=True)
    rounding_method = models.CharField(max_length=100,null=True)
    rounding_limit = models.IntegerField(blank=True, null=True, default=None)

    type_duty_tax = models.CharField(max_length=100,null=True)
    tax_type = models.CharField(max_length=100,null=True)
    valuation_type = models.CharField(max_length=100,null=True)
    rate_per_unit = models.IntegerField(blank=True, null=True, default=None)
    percentage_of_calcution = models.CharField(max_length=100,null=True)
    rond_method = models.CharField(max_length=100,null=True)
    rond_limit = models.IntegerField(blank=True, null=True, default=None)

    gst_applicable = models.CharField(max_length=100,null=True)
    setalter_gstdetails = models.CharField(max_length=20,null=True)
    type_of_supply = models.CharField(max_length=100,null=True)
    assessable_value = models.CharField(max_length=100,null=True)
    appropriate_to = models.CharField(max_length=100,null=True)
    method_of_calculation = models.CharField(max_length=100,null=True)

    balance_billbybill = models.CharField(max_length=100,null=True)
    credit_period = models.CharField(max_length=100,null=True)
    creditdays_voucher = models.CharField(max_length=100,null=True)


class sales(models.Model):
    no=models.AutoField(primary_key=True)
    particualrs=models.ForeignKey(tally_ledger,on_delete=models.CASCADE,null=True)
    Partyname=models.CharField(max_length=255)
    salesledger=models.CharField(max_length=255)
    item=models.CharField(max_length=255)
    rate=models.IntegerField()
    quantity=models.IntegerField()
    amount=models.IntegerField()
    total_amount=models.IntegerField()
       

    
  
    
class purchase(models.Model):
    no=models.AutoField(primary_key=True)
    particualrs=models.ForeignKey(tally_ledger,on_delete=models.CASCADE,null=True)
    invoiceno=models.IntegerField() 
    no=models.IntegerField()   
    partyname=models.CharField(max_length=225)
    purchaseledger=models.CharField(max_length=225)
    itemname=models.CharField(max_length=225)
    quantity=models.IntegerField() 
    rate=models.IntegerField()
    amount=models.IntegerField()
    total_amount=models.IntegerField()

class transactiontype(models.Model):
    transactiontype=models.CharField(max_length=225)

class Vouchertype(models.Model):
    vouchertype=models.CharField(max_length=255,null=True)

class account(models.Model):
     account=models.ForeignKey(tally_ledger,on_delete=models.CASCADE,null=True)
     date=models.DateTimeField()

class Particulars(models.Model):
    particualrs=models.ForeignKey(tally_ledger,on_delete=models.CASCADE,null=True)
    amount=models.IntegerField()

class bank(models.Model):
    ledger=models.ForeignKey(tally_ledger,on_delete=models.CASCADE,null=True)
    transactiontype=models.ForeignKey(transactiontype,on_delete=models.CASCADE,null=True)
    instno=models.IntegerField()
    instdate=models.DateField()
    amount=models.ForeignKey(Particulars,on_delete=models.CASCADE,null=True)
    date=models.ForeignKey(account,on_delete=models.CASCADE,null=True)
    vouchertype=models.ForeignKey(Vouchertype,on_delete=models.CASCADE,null=True)

