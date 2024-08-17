from django.db.models import Sum, Count
from django.shortcuts import render
from django.views import View

from .models import (
    Category,
    Institution,
    Donation
)

class LandingPage(View):
    def get(self, request, *args, **kwargs):
        quantity = Donation.objects.aggregate(total_quantity=Sum('quantity'))
        institutions = Donation.objects.aggregate(total_institutions=Count('institution'))
        context = {
            'quantity': quantity,
            'institutions': institutions,
        }
        return render(request, 'index.html', context)


class AddDonation(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'form.html')
    

class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')
    

class Register(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')
    
