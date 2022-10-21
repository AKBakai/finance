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
