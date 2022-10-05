from django.db.models import Q
from django.shortcuts import render

from app.news.models import News


def news_list(request):
    news_lists = News.objects.all()
    context = {
        'news_list': news_lists
    }
    return render(request, 'news/news_list.html', context)


def news_detail(request, id):
    news_detail = News.objects.get(id=id)
    return render(request, 'news/news_detail.html', {'news_detail': news_detail})


def search_1(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(title__icontains=q) | Q(paragraph__icontains=q))
        news_lists = News.objects.filter(multiple_q)
    else:
        news_lists = News.objects.all()
    return render(request, 'news/news_list.html', {'news_list': news_lists})