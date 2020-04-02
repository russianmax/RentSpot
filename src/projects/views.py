from django.shortcuts import render, redirect
from projects.models import Properties, Property_Applications, Property_Reviews
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreatingListingForm

def project_index(request):
    projects = Properties.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Properties.objects.get(pk=pk)
    applyButton = Property_Applications.objects.filter(listingId=project)
    propertyReview = Property_Reviews.objects.filter(property=project)
    if request.method == "POST":
        applyButton = Property_Applications(
            user=request.user,
            listingId=project,
        )
        applyButton.save()
    context = {'project': project, 'applyButton': applyButton, 'propertyReview': propertyReview}
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
            return redirect('/portal/', args=link.pk)
    else:
        listing_form = CreatingListingForm()
        link = listing_form

    return render(request, 'createListing.html', {'listing_form': link})

