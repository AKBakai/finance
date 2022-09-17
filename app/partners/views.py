from django.shortcuts import render


def partners(request):
    return render(request, 'ru/partners.html')
