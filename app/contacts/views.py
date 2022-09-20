from django.shortcuts import render, redirect

from app.home.form import FeedbackForm


def contacts(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FeedbackForm()
    return render(request, 'contacts/../../templates/contacts.html', {'form': form})
