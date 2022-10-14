from django.db.models import Q
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


def search_3(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(title__icontains=q) | Q(paragraph__icontains=q) | Q(text__icontains=q))
        financing = Financing.objects.filter(multiple_q)
    else:
        financing = Financing.objects.all()
    return render(request, 'financing/financing_list.html', {'financing': financing})