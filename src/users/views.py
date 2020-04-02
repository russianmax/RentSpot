from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from projects.models import Properties
from .models import Tenant_Profile, Tenant_Reviews

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('portal')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.tenant_profile)
        messages.success(request, f'in the else statement')
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)

@login_required
def landlordPortal(request):
    user = request.user
    portal = Properties.objects.filter(landlord=user)
    context = {
        'portal': portal
    }
    return render(request, 'users/landlordPortal.html', context)

@login_required
def viewProfile(request, pk):
    portal = Tenant_Profile.objects.get(pk=pk)
    tenantReview = Tenant_Reviews.objects.filter(tenant=portal)
    context = {
        'portal': portal,
        'tenantReview': tenantReview
    }
    return render(request, 'users/view_profile.html', context)

