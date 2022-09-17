from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
import requests
from bs4 import BeautifulSoup

from app.home.models import Carousel
from app.home.form import FeedbackForm

url = 'https://www.nbkr.kg/index.jsp?lang=RUS'


def home(request):
    trans = translate(language='ru')
    carousel_list = Carousel.objects.all()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FeedbackForm()
    sourse = requests.get(url)
    main_text = sourse.text
    soup = BeautifulSoup(main_text)
    div = soup.find('div', {'id': 'sticker-exrates'})
    tr = div.find('span', {'class': 'gold-date'})
    tr1 = div.findAll('td', {'class': 'exrate'})
    tr = tr.text
    a = []
    for i in tr1:
        if tr1.index(i) % 2 != 0:
            i = i.text
            a.append(i)
    context = {
        'carousel_list': carousel_list,
        'trans': trans,
        'form': form,
        'date': tr,
        'exrate': a[0],
        'exrate1': a[1],
        'exrate2': a[2],
        'exrate3': a[3]
    }
    return render(request, 'index.html', context)


def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('hello')
    finally:
        activate(cur_language)
    return text