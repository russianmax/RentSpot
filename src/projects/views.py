from django.shortcuts import render, redirect
from projects.models import Properties, Property_Applications, Property_Reviews
from users.models import Landlord_Profile, Tenant_Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import modelformset_factory
from .forms import CreatingListingForm, ListingApplicationForm, PropertyReviewForm ,ScheduleViewingForm, ManageListingForm
from .filters import CountyFilter



def project_index(request):
    # search_term = ''
    # if 'search' in request.GET:
    #     search_term = request.GET['search']
    #     projects = Properties.objects.all().filter(street1__icontains=search_term)
    projects = Properties.objects.all()
    user = request.user
    myFilter = CountyFilter(request.GET, queryset=projects)
    projects = myFilter.qs
    context = {
        'projects': projects, 'myFilter' : myFilter,
    }
    return render(request, 'project_index.html', context)


# @login_required
def scheduleViewing(request,pk):
    landlord = request.user.landlord_profile
    submitButton = ScheduleViewingForm(request.POST)
    viewingApply = Property_Applications.objects.get(pk=pk)
    if request.method == 'POST':
        link = submitButton.save(commit=False)
        link.landlord = landlord
        link.listing = viewingApply.listing
        print(viewingApply)
        messages.success(request, f'You have Scheduled a viewing!')
        return redirect('/portal/')
    else:
        return redirect('/portal/')

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

def project_detail(request, pk):
    project = Properties.objects.get(pk=pk)
    applyButton = Property_Applications.objects.filter(listing=project)
    propertyReview = Property_Reviews.objects.filter(property=project)
    context = {'project': project, 'propertyReview': propertyReview}

    if request.user.last_name == 'False':
        tenant_profile = Tenant_Profile.objects.get(tenant=request.user.tenant_profile.tenant_id)
        if request.method == "POST":
            applyButton = Property_Applications(
                user=request.user,
                listing=project,)
            applyButton.save()
        context['applyButton'] = applyButton
        context['tenant_profile']= tenant_profile
    elif request.user.landlord_profile.landlord_id == project.landlord_id:
        change_listing_form = ManageListingForm(request.POST, request.FILES, instance=project)
        if request.method == 'POST':
            if change_listing_form.is_valid():
                change_listing_form.save()
                messages.success(request, f'Your account has been updated!')
        context['change_listing_form'] = change_listing_form

    return render(request, 'project_detail.html', context)



# @login_required
# def createListing(request):
#     ImageFormset = modelformset_factory(Properties, fields=('images',), extra=5)
#     if request.method == 'POST':
#         listing_form = CreatingListingForm(request.POST)
#         formset = ImageFormset(request.POST or None, request.FILES or None)
#         if listing_form.is_valid() and formset.is_valid():
#             link  = listing_form.save(commit=False)
#             link.landlord = request.user
#             link.save()
#             for f in formset:
#                 print(len(formset))
#                 try:
#                     photo = Properties(properties=request.user.landlord_profile,images=f.clean_data['images'])
#                     photo.save()
#                     messages.success(request, f'Your listing has been created!!')
#                     return redirect('/portal/', args=link.pk)
#                 except Exception as e:
#                     break
#     else:
#         listing_form = CreatingListingForm()
#         formset = ImageFormset ()
#         link = listing_form
#     return render(request, 'createListing.html', {'listing_form': link,'formset':formset})

@login_required
def createListing(request):

    if request.method == 'POST':
        listing_form = CreatingListingForm(request.POST, request.FILES)
        if listing_form.is_valid():
            link  = listing_form.save(commit=False)
            link.landlord = request.user
            link.save()
            messages.success(request, f'Your listing has been created!!')
            return redirect('/portal/', args=link.pk)
    else:
        listing_form = CreatingListingForm()
        link = listing_form

    return render(request, 'createListing.html', {'listing_form': link})
