from django.shortcuts import render


def sharia_board(request):
    return render(request, 'ru/sharia_board.html')
