from django.shortcuts import render, redirect
from projects.models import Listing_Database
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreatingListingForm

def project_index(request):
    projects = Listing_Database.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Listing_Database.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

@login_required
def createListing(request):
    if request.method == 'POST':
        listing_form = CreatingListingForm(request.POST, request.FILES)
        if listing_form.is_valid():
            link  = listing_form.save(commit=False)
            link.user = request.user
            link.save()
            messages.success(request, f'Your listing has been created!!')
            return redirect('/profile/')
    else:
        listing_form = CreatingListingForm()
        link = listing_form

    return render(request, 'createListing.html', {'listing_form': link})

# @login_required
# def createListing(request):
#     listings = Listing_Database.objects.all()
#     context = {
#         'listings': listings
#     }
#     if request.method == 'POST':
#         if request.POST.get('address') and request.POST.get('rentPrice') and request.POST.get('description')and request.POST.get('bedRooms') and request.POST.get('bathRoom'):
#             post = Listing_Database()
#             post.user = request.user
#             post.address = request.POST.get('address')
#             post.rentPrice = request.POST.get('rentPrice')
#             post.description = request.POST.get('description')
#             post.bedRooms= request.POST.get('bedRooms')
#             post.bathRoom= request.POST.get('bathRoom')
#             post.tenantCondtions = request.POST.get('tenantCondtions')
#             # post.image = request.POST.get('image')
#             post.save()
#             messages.success(request, f'Your listing has been created!!')
#             return redirect('createListing')
        
        
#     return render(request, 'createListing.html', context)
