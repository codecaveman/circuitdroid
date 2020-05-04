from django.shortcuts import render

# Create your views here.
from .models import Congregation


def index(request):
    context = {"name": "Frank"}

    return render(request, 'congregation/index.html', context)
