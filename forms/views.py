from django.shortcuts import render

# Create your views here.
import os.path
from django.http import HttpResponse
from .models import Video
from django.shortcuts import render
from .models import Video
def index(request):
    firstvideo = Video.objects.last()
    videofile = os.path.join(BASE_DIR, 'media')
    form = VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    else:
        pass
    context = {'file_url': videofile,
               'form': form
               }
    respomse= render(request, 'index.html', context)
    return respomse
