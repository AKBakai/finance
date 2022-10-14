from django.db.models import Q
from django.shortcuts import render

from app.partners.models import Partners


def partners(request):
    partners = Partners.objects.all()
    return render(request, 'partners.html', {'partners': partners})

# def search_6(request):
#     if 'q' in request.GET:
#         q = request.GET['q']
#         multiple_q = Q(Q(title__icontains=q) | Q(text__icontains=q))
#         partners = Partners.objects.filter(multiple_q)
#     else:
#         partners = Partners.objects.all()
#     return render(request, 'partners.html', {'partners': partners})
