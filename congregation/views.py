from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Congregation


def index(request):
    congregations = Congregation.objects.all()
    context = {"congregations": congregations}

    return render(request, 'congregation/index.html', context)


def detail(request, congregation_id):
    congregation = get_object_or_404(Congregation, pk=congregation_id)
    return render(request, 'congregation/detail.html', {'congregation': congregation})
