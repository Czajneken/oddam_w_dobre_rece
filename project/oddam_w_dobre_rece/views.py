import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Sum, Count
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from .models import (
    Category,
    Institution,
    Donation
)

from .forms import (
    DonationToCharityForm,
    EditUserForm,
    EditUserPasswordForm,
)

class LandingPage(View):
    def get(self, request, *args, **kwargs):
        gifts_quantity = Donation.objects.aggregate(total_quantity=Sum('quantity'))
        gifted_institutions = Donation.objects.aggregate(total_institutions=Count('institution'))
        
        all_foundations = Institution.objects.filter(type=1)
        all_non_gov_organizations = Institution.objects.filter(type=2)
        all_localraisers = Institution.objects.filter(type=3)

        context = {
            'gifts_quantity': gifts_quantity,
            'gifted_institutions': gifted_institutions,
            'all_foundations': all_foundations,
            'all_non_gov_organizations': all_non_gov_organizations,
            'all_localraisers': all_localraisers,
        }
        return render(request, 'index.html', context)


class AddDonation(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, *args, **kwargs):
        form = DonationToCharityForm
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        context = {
            'categories': categories,
            'institutions': institutions,
            'form': form,
        }
        return render(request, 'form.html', context)

    def post(self, request, *args, **kwargs):
        form = DonationToCharityForm(request.POST)
        if form.is_valid():
            user = request.user.id
            institution = request.POST['institution']
            donation = Donation.objects.create(**form.cleaned_data, user_id=user, institution_id=institution)
            categories = request.POST.getlist('categories')
            for category in categories:
                donation.categories.add(category)
            return render(request, 'form-confirmation.html')
        else:
            categories = Category.objects.all()
            institutions = Institution.objects.all()
            context = {
                'categories': categories,
                'institutions': institutions,
                'form': form,
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
    

class Profile(View):
    def get(self, request, *args, **kwargs):
        user = request.user.id
        all_user_donations = Donation.objects.filter(user=user)

        context = {
            'all_user_donations': all_user_donations
        }

        return render(request, 'profile.html', context)
    def post(self, request, *args, **kwargs):
        user = request.user.id
        donation_id = request.POST.get('donation_id')
        donation_is_taken = request.POST.get('is_taken')

        edit_donation = Donation.objects.get(user=user, pk=donation_id)
        edit_donation.is_taken = donation_is_taken
        edit_donation.save()

        return redirect('profile')


class EditUser(View):
    def get(self, request, *args, **kwargs):
        form = EditUserForm
        form2 = EditUserPasswordForm
        context = {
            'form': form,
            'form2': form2,
        }
        return render(request, 'edit_user.html', context)

    def post(self, request, *args, **kwargs):
        form = EditUserForm(request.POST)
        form2 = EditUserPasswordForm(request.POST)
        if form.is_valid():
            user_id = request.user.id
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']

            user = User.objects.get(pk=user_id)
            user.username = email
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()

            return redirect('profile')
        elif form2.is_valid():
            user_username = request.user.username
            password = request.POST['password']

            user = User.objects.get(username=user_username)
            user.set_password = password
            user.save()
            return redirect('logout')
        else:
            return redirect('edit_user')