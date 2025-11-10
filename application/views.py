from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    carousel_images = CarouselImage.objects.all() 
    videos = Video.objects.all()
    context = {
        'carousel_images': carousel_images, 
        'videos': videos
        }
    return render(request, 'home.html', context) 
 
def video(request):
    videos = Video.objects.get()
    return render(request, 'home.html', {'videos': videos})

def contactus(request):
    return render(request, 'contactus.html')