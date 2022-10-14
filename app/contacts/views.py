from django.db.models import Q
from django.shortcuts import render, redirect

from app.contacts.models import Contacts
from app.home.form import FeedbackForm


def contacts(request):
    contacts = Contacts.objects.all()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FeedbackForm()
    context = {'form': form,
               'contacts': contacts,
    }
    return render(request, 'contacts.html', context)


# def search_2(request):
#     if 'q' in request.GET:
#         q = request.GET['q']
#         multiple_q = Q(Q(title__icontains=q) | Q(text__icontains=q))
#         contacts = Contacts.objects.filter(multiple_q)
#     else:
#         contacts = Contacts.objects.all()
#     return render(request, 'contacts.html', {'contacts': contacts})
