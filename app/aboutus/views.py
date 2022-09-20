from django.shortcuts import render


def about_us(request):
    return render(request, 'ru/../../templates/aboutus.html')