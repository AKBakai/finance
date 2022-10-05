from django.shortcuts import render

from app.financing.models import Financing


def financing_list(request):
    financing = Financing.objects.all()
    context = {
        'financing': financing
    }
    return render(request, 'financing/financing_list.html', context)


def financing_detail(request, id):
    financing_detail = Financing.objects.get(id=id)
    context = {
        'financing_detail': financing_detail,
    }
    return render(request, 'financing/financing_detail.html', context)
