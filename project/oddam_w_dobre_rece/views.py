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
        gifts_quantity = Donation.objects.aggregate(total_quantity=Sum('quantity'))
        gifted_institutions = Donation.objects.aggregate(total_institutions=Count('institution'))
        
        all_foundations = Institution.objects.filter(type=1)
        all_organisations = Institution.objects.filter(type=2)
        all_localraisers = Institution.objects.filter(type=3)

        context = {
            'gifts_quantity': gifts_quantity,
            'gifted_institutions': gifted_institutions,
            'all_foundations': all_foundations,
            'all_organisations': all_organisations,
            'all_localraisers': all_localraisers,
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
    
