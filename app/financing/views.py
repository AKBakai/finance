from django.shortcuts import render


def financing_list(request):
    return render(request, 'financing/financing_list.html')


def financing_detail(request):
    return render(request, 'financing/financing_detail.html')
