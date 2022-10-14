from django.db.models import Q
from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup

from app.financing.models import Financing
from app.home.models import Carousel, AboutUsShort, ContactUsShort
from app.home.form import FeedbackForm
from app.news.models import News

url = 'https://www.nbkr.kg/index.jsp?lang=RUS'


def home(request):
    carousel_list = Carousel.objects.all()
    about_us_short = AboutUsShort.objects.filter().order_by('-id')[:1]
    contacts_data = ContactUsShort.objects.filter().order_by('-id')[:1]
    news_list = News.objects.filter().order_by('-id')[:4]
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
        'about_us_short': about_us_short,
        'contacts_data': contacts_data,
        'news_list': news_list,
        'form': form,
        'date': tr,
        'exrate': a[0],
        'exrate1': a[1],
        'exrate2': a[2],
        'exrate3': a[3]
    }
    return render(request, 'index.html', context)


def search_5(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(title__icontains=q) | Q(paragraph__icontains=q) | Q(text__icontains=q))
        carousel_list = Carousel.objects.filter(multiple_q)
        about_us_short = AboutUsShort.objects.filter(multiple_q)
        contacts_data = ContactUsShort.objects.filter(multiple_q)
        news_list = News.objects.filter(multiple_q)
    else:
        carousel_list = Carousel.objects.all()
        about_us_short = AboutUsShort.objects.all()
        contacts_data = ContactUsShort.objects.all()
        news_list = News.objects.all()
    context = {
        'carousel_list': carousel_list,
        'about_us_short': about_us_short,
        'contacts_data': contacts_data,
        'news_list': news_list
    }
    return render(request, 'index.html', context)