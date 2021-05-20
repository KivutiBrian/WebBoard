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
