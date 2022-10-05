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
