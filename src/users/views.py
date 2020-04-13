from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .forms import UserRegistrationForm, UserUpdateForm, TenantProfileUpdateForm , LandlordProfileUpdateForm 
from projects.models import Properties, Property_Applications
from .models import Tenant_Profile, Tenant_Reviews, Landlord_Profile
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
                return redirect('tenantportal')
            else:
                if p_form.is_valid():
                    p_form.save()
                    return redirect('landlordportal')
    else:
        if request.user.last_name == 'False':
            p_form = TenantProfileUpdateForm(instance=request.user.tenant_profile)
        else:
            p_form = LandlordProfileUpdateForm(instance=request.user.landlord_profile)
            messages.success(request, f'Click "Update" to store your details')
    context = {'p_form': p_form, }
    return render(request, 'users/profile.html', context)


@login_required
def landlordPortal(request,):
    user = request.user
    landlord_user = request.user.landlord_profile
    print(landlord_user)
    portal = Properties.objects.filter(landlord=user)
    tenantApplicant = Property_Applications.objects.filter(property_owner=landlord_user)

    context = {
        'portal': portal,
        'tenantApplicant':tenantApplicant
    }
    return render(request, 'users/landlordPortal.html', context)


@login_required
def tenantPortal(request):
    user = request.user
    tenant_user = request.user.tenant_profile
    application = Property_Applications.objects.filter(tenant_apply=tenant_user)
    context = {
        'application':application
    }
    return render(request, 'users/tenantPortal.html', context)


@login_required
def viewProfile(request, pk):
    landlord_user = request.user.landlord_profile
    portal = Tenant_Profile.objects.get(pk=pk)
    tenantReview = Tenant_Reviews.objects.filter(tenant=portal)
    viewingApplication = Property_Applications.objects.filter(property_owner=landlord_user)
    context = {
        'portal': portal,
        'tenantReview': tenantReview,
    }
    return render(request, 'users/view_profile.html', context)

def documents(request):
    context = {}
    if request.method == 'POST':
        uploaded_document = request.FILES['document']
        #print(uploaded_document.name, uploaded_document.size)
        fs = FileSystemStorage()
        name = fs.save(uploaded_document.name,uploaded_document)
        context['url'] = fs.url(name)
    return render(request, 'users/documents.html', context)

