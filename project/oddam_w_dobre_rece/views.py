from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Sum, Count
from django.shortcuts import render, redirect
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


class AddDonation(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, *args, **kwargs):
        donation_categories = Category.objects.all()

        context = {
            'donation_categories': donation_categories,
        }

        return render(request, 'form.html', context)
    

class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')
    def post(self, request, *args, **kwargs):
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return redirect('register')
    

class Logout(View):
     def get(self, request, *args, **kwargs):
         logout(request)
         return redirect('main')


class Register(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password2')

        context = {
            'name': name,
            'surname': surname,
            'email': email,
            'pass1': pass1,
            'pass2': pass2,
        }

        if pass1 == pass2:
            user = User.objects.create_user(username=email, first_name=name, last_name=surname, email=email, password=pass1)
            user.save()
            return redirect('login')
        else:
            return render(request, 'register.html', context)
    
