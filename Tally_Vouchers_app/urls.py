from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('purchase',views.purchase,name='purchase'),
    path('sales',views.sales,name='sales'),
]
