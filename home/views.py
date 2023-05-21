from django.shortcuts import render, redirect
from .models import sbentry
import os

# Create your views here.
def home(request):
    entries = sbentry.objects.all().order_by('-submit_date')
    context = {'entries': entries}
    return render(request, 'home.html', context)

from .models import sbentry
from django.shortcuts import render

def submit(request):
    entries = sbentry.objects.all().order_by('-submit_date')
    context = {'entries': entries}

    if request.method == "POST":
        name = request.POST['name']
        link = request.POST['link']
        featured_image = None

        if 'featured_image' in request.FILES:
            featured_image = request.FILES['featured_image']

        try:
            old_entries = sbentry.objects.filter(name=name)
            for old_entry in old_entries:
                if old_entry.featured_image:
                    # Delete the old featured image file from the static folder
                    os.remove(old_entry.featured_image.name)
            old_entries.delete()
        except sbentry.DoesNotExist:
            pass

        new_entry = sbentry(name=name, link=link, featured_image=featured_image)
        new_entry.save()

        return redirect('home')
    else:
        return render(request, 'submit.html', context)
