from django.shortcuts import render, get_object_or_404, redirect
from .models import Link

# Create your views here.
def index(request):
    links = Link.objects.all()
    context = {
        'links': links
    }
    return render(request, 'links/index.html', context)

def root_link(request, link_slug):
    link = get_object_or_404(Link, slug=link_slug)
    link.click() #this will increment the clicked field
    
    return redirect(link.url)
   