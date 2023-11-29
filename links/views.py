from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Link
from .forms import LinkForm

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


def add_link(request):
    # Detta kommer att ske när man trycker på create
    if request.method == 'POST':
        #form has data
        form = LinkForm(request.POST)
        if form.is_valid():
            #save the data & return user to homepage.
            form.save()
            return redirect(reverse('home'))
    else:
        # Detta kommer upp innan man trycker på create
        form = LinkForm()
    context = {
        'form': form
    }
    return render(request, 'links/create.html', context)