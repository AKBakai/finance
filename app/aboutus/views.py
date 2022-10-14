from django.shortcuts import render
from django.db.models import Q
from app.aboutus.models import AboutUs


def about_us(request):
    about_us = AboutUs.objects.all()
    context = {
        'aboutus': about_us,
    }
    return render(request, 'aboutus.html', context)


def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(title__icontains=q) | Q(text__icontains=q))
        about_us = AboutUs.objects.filter(multiple_q)
    else:
        about_us = AboutUs.objects.all()
    return render(request, 'aboutus.html', {'aboutus': about_us})