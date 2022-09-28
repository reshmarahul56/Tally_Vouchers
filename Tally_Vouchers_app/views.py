from django.shortcuts import render

from Tally_Vouchers_app.models import bank, tally_ledger

# Create your views here.

def home(request):
    return render(request,'base.html')

def purchase(request):
    bak=bank.objects.all()
    # con=contra.objecs.all()
    led=tally_ledger.objects.all()
    return render(request,'purchase.html',{'bak':bak,'led':led})
def sales(request):
    bak=bank.objects.all()
    # con=contra.objects.all()
    led=tally_ledger.objects.all()
    return render(request,'sales.html',{'bak':bak,'led':led})

