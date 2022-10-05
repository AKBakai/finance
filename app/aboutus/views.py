from django.shortcuts import render

from app.aboutus.models import AboutUs


def about_us(request):
    about_us = AboutUs.objects.all()
    context = {
        'aboutus': about_us,
    }
    return render(request, 'aboutus.html', context)