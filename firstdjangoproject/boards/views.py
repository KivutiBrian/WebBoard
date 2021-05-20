from django.shortcuts import render
from django.http import HttpResponse

# models
from .models import Board

# Create your views here.
def index(request):

    boards = Board.objects.all()

    context = {
        'boards': boards
    }

    return render(request, 'boards/boards.html', context=context)

def boards_topic(request, board_id):

    context = {
        'board_id': board_id
    }

    return render(request, 'boards/boards_topic.html', context=context)
