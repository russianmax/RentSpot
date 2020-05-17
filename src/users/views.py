from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .forms import UserRegistrationForm, UserUpdateForm, TenantProfileUpdateForm , LandlordProfileUpdateForm , AddGuarantorForm
from projects.models import Properties, Property_Applications , Schedule_Viewing
from projects.forms import ScheduleViewingForm
from .models import Tenant_Profile, Tenant_Reviews, Landlord_Profile, Guarantor
from django import forms

def register(request):
    # allows users to register
    # UserRegistrationForm is used to collect data, like username, password etc
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            last_name = form.cleaned_data.get('last_name')
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def guarantor(request,):
    tenant_user = request.user.tenant_profile
    if request.method == 'POST':
        # add a guarantor form collects guarantor data such as guarantor salary
        addG = AddGuarantorForm(request.POST, request.FILES)
        if addG.is_valid():
            link = addG.save(commit=False)
            link.tenant = tenant_user
            link.save()
            messages.success(request, f"You've added a guarantor to your profile!")
            # once a guarantor is added to tenant profile
            # guarantors salary and tenants salary float fields are combined
            # both_salary within Tenant_Profile model then contains their salaries
            guarantor = Guarantor.objects.get(tenant=tenant_user).g_salary
            tenant = Tenant_Profile.objects.get(tenant=request.user)
            tenant.both_salary = tenant.salary + guarantor
            tenant.save()
            return redirect('/portal/')
    else:
        addG = AddGuarantorForm()
        link = addG
    return render(request, 'users/documents.html', {'addG': link})



@login_required
# simple profile function that allows users to update their profiles - username, profile pic etc
# TenantProfileUpdateForm and LandlordProfileUpdateForm are displayed based on the usertype thats authenicated
# for tenant users they can upload documents
# landlords users can add in their address
def profile(request, *args, **kwargs):
    if request.method == 'POST':
        if request.user.last_name == 'False':
            p_form = TenantProfileUpdateForm(request.POST, request.FILES, instance=request.user.tenant_profile)
        else:
            p_form = LandlordProfileUpdateForm(request.POST, request.FILES, instance=request.user.landlord_profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            if request.user.last_name == 'False':
                return redirect('portal')
            else:
                if p_form.is_valid():
                    p_form.save()
                    return redirect('portal')
    else:
        if request.user.last_name == 'False':
            p_form = TenantProfileUpdateForm(instance=request.user.tenant_profile)
            messages.info(request, f'Click "Update" to store your details')
        else:
            p_form = LandlordProfileUpdateForm(instance=request.user.landlord_profile)
            messages.info(request, f'Click "Update" to store your details')
    context = {'p_form': p_form, }
    return render(request, 'users/profile.html', context)

@login_required
def portal(request,):
    # based on usertype, displays Tenant or Landlord portal
    user = request.user
    # Landlord
    if user.last_name == 'True':
        landlord_user = request.user.landlord_profile
        properties = Properties.objects.filter(landlord=user)
        applications = Property_Applications.objects.filter(property_owner=landlord_user)
        print(applications)
        viewings = Schedule_Viewing.objects.filter(landlord=landlord_user)

        context = {'properties': properties,
                   'applications':applications,
                   'viewings' : viewings, }
        return render(request, 'users/landlordPortal.html', context)
    #Tenant
    else:
        tenant_user = request.user.tenant_profile
        applications = Property_Applications.objects.filter(tenant_apply=tenant_user)
        viewings = Schedule_Viewing.objects.filter(tenant=tenant_user)
        context = {
            'applications': applications,
            'viewings' : viewings
        }
        return render(request, 'users/tenantPortal.html', context)

@login_required
# function that allows landlords to schedule viewings with tenants
# ScheduleViewingForm allows landlords to schedule viewing with the applicaints
# this form takes the data and time of the viewing
def viewProfile(request, pk, listing):
    landlord_user = request.user.landlord_profile
    tenant = Tenant_Profile.objects.get(pk=pk)
    tenantReview = Tenant_Reviews.objects.filter(tenant=tenant)
    #property method only returns on property object as listing ID is passed through the function
    property = Properties.objects.get(pk=listing)
    submitButton = ScheduleViewingForm(request.POST)
    if request.method == 'POST':
        link = submitButton.save(commit=False)
        link.landlord = landlord_user
        link.listing = property
        link.tenant = tenant
        link.save()
        messages.success(request, f'Your scheduled a viewing!')
        viewingApply = Property_Applications.objects.get(pk=pk)
        viewingApply.viewing_scheduled = True
        print(viewingApply.viewing_scheduled)
        viewingApply.save()
        return redirect('portal')
    else:
        link = submitButton

    context = {
        'tenant': tenant,
        'tenantReview': tenantReview,
        'submitButton': link
    }
    return render(request, 'users/view_profile.html', context)






