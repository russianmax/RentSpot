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
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            last_name = form.cleaned_data.get('last_name')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


# def guarantor(request,):
#     addG = AddGuarantorForm(request.POST, request.FILES, instance=request.user.tenant_profile)
#     if request.method == 'POST':
#         if addG.is_valid():
#             link = addG.save(commit=False)
#             link.tenant = request.user
#             link.save()
#             messages.success(request, f"You've added a guarantor to your profile!")
#         else:
#             link  = addG
#             messages.info(request,'Please upload the required files.')
#
#     context = {'addG': addG}
#
#     return render(request, 'users/documents.html', context)

def guarantor(request,):
    # new field created in DB called both_salary
    # this code adds both salaries and displays it in both_salary
    # does it everytime this view is clicked
    tenant_user = request.user.tenant_profile
    if request.method == 'POST':
        addG = AddGuarantorForm(request.POST, request.FILES)
        if addG.is_valid():
            link = addG.save(commit=False)
            link.tenant = tenant_user
            link.save()
            messages.success(request, f"You've added a guarantor to your profile!")
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
    user = request.user
    # Landlord
    if user.last_name == 'True':
        landlord_user = request.user.landlord_profile
        properties = Properties.objects.filter(landlord=user)
        applications = Property_Applications.objects.filter(property_owner=landlord_user)
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

# need to add schedule viewing functionality here
@login_required
def viewProfile(request, pk, listing):
    landlord_user = request.user.landlord_profile
    tenant = Tenant_Profile.objects.get(pk=pk)
    tenantReview = Tenant_Reviews.objects.filter(tenant=tenant)
    viewingApplication = Property_Applications.objects.filter(property_owner=landlord_user,tenant_apply=tenant)
    property = Properties.objects.get(pk=listing)
    submitButton = ScheduleViewingForm(request.POST)
    if request.method == 'POST':
        link = submitButton.save(commit=False)
        link.landlord = landlord_user
        link.listing = property
        link.tenant = tenant
        link.save()
        messages.success(request, f'Your scheduled a viewing!')
        return redirect('portal')
    else:
        link = submitButton

    context = {
        'tenant': tenant,
        'tenantReview': tenantReview,
        'submitButton': link
    }
    return render(request, 'users/view_profile.html', context)


# @login_required
# def viewProfile(request, pk):
#     landlord_user = request.user.landlord_profile
#     portal = Tenant_Profile.objects.get(pk=pk)
#     tenantReview = Tenant_Reviews.objects.filter(tenant=portal)
#     viewingApplication = Property_Applications.objects.filter(property_owner=landlord_user)
#     context = {
#         'portal': portal,
#         'tenantReview': tenantReview,
#     }
#     return render(request, 'users/view_profile.html', context)



