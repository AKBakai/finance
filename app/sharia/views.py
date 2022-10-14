from django.db.models import Q
from django.shortcuts import render

from app.sharia.models import ShariaBoard, ShariaBoardInfo


def sharia_board(request):
    sharia = ShariaBoard.objects.all()
    info = ShariaBoardInfo.objects.all()
    context = {
        'sharia_board': sharia,
        'sharia_info': info
    }
    return render(request, 'sharia_board.html', context)


# def search_7(request):
#     if 'q' in request.GET:
#         q = request.GET['q']
#         multiple_q = Q(Q(title__icontains=q) | Q(text__icontains=q))
#         sharia = ShariaBoard.objects.filter(multiple_q)
#     else:
#         sharia = ShariaBoard.objects.all()
#     return render(request, 'sharia_board.html', {'sharia': sharia})
