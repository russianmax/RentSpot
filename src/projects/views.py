from django.shortcuts import render, redirect
from projects.models import Properties, Property_Applications, Property_Reviews
from users.models import Landlord_Profile, Tenant_Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreatingListingForm, ListingApplicationForm

def project_index(request):
    projects = Properties.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def property_apply(request, pk):
    project = Properties.objects.get(pk=pk)
    applyButton = ListingApplicationForm(request.POST)
    propertyReview = Property_Reviews.objects.filter(property=project)
    landlord_table = Landlord_Profile.objects.get(landlord=project.landlord)
    profile = request.user.tenant_profile
    if request.method == "POST":
        link = applyButton.save(commit=False)
        link.tenant_apply = profile
        link.property_owner = landlord_table
        link.listing=project
        link.save()
        messages.success(request, f'You have applied!')
        return redirect('/tenantportal/')
    else:
        link = applyButton
    context = {'project': project, 'applyButton': link, 'propertyReview': propertyReview}
    return render(request, 'application_submit.html', context)

def project_detail(request, pk):
    project = Properties.objects.get(pk=pk)
    applyButton = Property_Applications.objects.filter(listing=project)
    propertyReview = Property_Reviews.objects.filter(property=project)
    if request.method == "POST":
        applyButton = Property_Applications(
            user=request.user,
            listing=project,
        )
        applyButton.save()
    context = {'project': project,
               'applyButton': applyButton,
               'propertyReview': propertyReview}
    return render(request, 'project_detail.html', context)

@login_required
def createListing(request):
    if request.method == 'POST':
        listing_form = CreatingListingForm(request.POST, request.FILES)
        if listing_form.is_valid():
            link  = listing_form.save(commit=False)
            link.landlord = request.user
            link.save()
            messages.success(request, f'Your listing has been created!!')
            return redirect('/landlordportal/', args=link.pk)
    else:
        listing_form = CreatingListingForm()
        link = listing_form

    return render(request, 'createListing.html', {'listing_form': link})

