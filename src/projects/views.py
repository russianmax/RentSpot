from django.shortcuts import render, redirect
from projects.models import Properties, Property_Applications, Property_Reviews,Property_Images
from users.models import Landlord_Profile, Tenant_Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import modelformset_factory
from .forms import CreatingListingForm, ListingApplicationForm, PropertyReviewForm ,ScheduleViewingForm, ManageListingForm,ImageForm
from .filters import Filter


def project_index(request):
    # displays all properties available on the site
    projects = Properties.objects.all()
    # myFilter allows to filter properties based on location, bedrooms, bathrooms and type of property
    myFilter = Filter(request.GET, queryset=projects)
    projects = myFilter.qs
    context = {
        'projects': projects, 'myFilter': myFilter,
    }
    return render(request, 'project_index.html', context)


# allows tenants to leave property reviews
def property_review(request,pk):
    project = Properties.objects.get(pk=pk)
    reviewButton = PropertyReviewForm(request.POST)
    landlord_table = Landlord_Profile.objects.get(landlord=project.landlord_id)
    profile = request.user.tenant_profile
    if request.method == "POST":
        link = reviewButton.save(commit=False)
        link.tenant = profile
        link.property = project
        link.landlord = landlord_table
        link.save()
        messages.success(request, f'Thanks for leaving a review!')
        return redirect ('/portal/')
    else:
        link = reviewButton
    context = {
        'project': project,
        'reviewButton': link
    }
    return render(request, 'review_submit.html', context)

# allows tenants to apply for a property
def property_apply(request, pk):
    project = Properties.objects.get(pk=pk)
    applyButton = ListingApplicationForm(request.POST)
    propertyReview = Property_Reviews.objects.filter(property=project)
    landlord_table = Landlord_Profile.objects.get(landlord=project.landlord_id)
    profile = request.user.tenant_profile
    if request.method == "POST":
        link = applyButton.save(commit=False)
        link.tenant_apply = profile
        link.property_owner = landlord_table
        link.listing=project
        link.save()
        messages.success(request, f'You have applied!')
        return redirect('/portal/')
    else:
        link = applyButton
        messages.info(request, 'When you apply you agree to sharing your profile information with the property owner.')
    context = {'project': project, 'applyButton': link, 'propertyReview': propertyReview}
    return render(request, 'application_submit.html', context)

def project_detail(request,pk, *args, **kwargs):
    project = Properties.objects.get(pk=pk)
    applyButton = Property_Applications.objects.filter(listing=project)
    propertyReview = Property_Reviews.objects.filter(property=project)
    # getting the urls
    property_images = Property_Images.objects.filter(property=project)
    # context that's displayed to all users
    context = {
        'project': project,
        'propertyReview': propertyReview,
        'property_images' : property_images,
           }
    if request.user.is_authenticated:
        if request.user.last_name == 'False': # allows to tenant to view ads and apply for them if they meet the requirements
            tenant_profile = Tenant_Profile.objects.get(tenant=request.user.tenant_profile.tenant_id)
            if request.method == "POST":
                applyButton = Property_Applications(
                    user=request.user,
                    listing=project,)
                applyButton.save()
            # adding more relevant context if user is tenant
            context['applyButton'] = applyButton
            context['tenant_profile']= tenant_profile
        if request.user.last_name == 'True':
            if request.user.landlord_profile.landlord_id == project.landlord_id: # if the landlord owns this ad, this let's him edit the ad
                if request.method == 'POST':
                    # ManageMyListingForm allows landlords to edit info about their properties - property can also be paused
                    change_listing_form = ManageListingForm(request.POST, request.FILES,instance=project)
                    if change_listing_form.is_valid():
                        change_listing_form.landlord = request.user.landlord_profile
                        change_listing_form.save()
                        messages.success(request, f'Your account has been updated!')
                else:
                    change_listing_form = ManageListingForm(instance=project)
                    messages.info(request, f'Click "Manage My Spot" to pause or edit listing details')
                context['change_listing_form'] = change_listing_form
    return render(request, 'project_detail.html', context)


@login_required
def createListing(request):
    if request.method == 'POST':
        # listing form collects basic data about the property
        listing_form = CreatingListingForm(request.POST, request.FILES)
        # allows to upload multiple images per property
        image_form = ImageForm(request.POST, request.FILES)
        images = request.FILES.getlist('images')
        if listing_form.is_valid() and image_form.is_valid():
            link  = listing_form.save(commit=False)
            link.landlord = request.user
            link.save()
            # links property images to the Property_Images object
            for i in images:
                image_instance = Property_Images(images=i, property=link)
                image_instance.save()
            messages.success(request, f'Your listing has been created!!')
            return redirect('/portal/', args=link.pk)
    else:
        listing_form = CreatingListingForm()
        link = listing_form
        image_form = ImageForm()

    return render(request, 'createListing.html', {'listing_form': link,'image_form': image_form})

