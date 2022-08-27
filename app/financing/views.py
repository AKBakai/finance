from django.shortcuts import render


def financing(request):
    return render(request, 'ru/credit/financing.html')
