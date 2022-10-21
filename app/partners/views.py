from django.shortcuts import render
from app.partners.models import Partners


def partners(request):
    partners = Partners.objects.all()
    return render(request, 'partners.html', {'partners': partners})
