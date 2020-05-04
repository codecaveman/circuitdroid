from django.shortcuts import render

# Create your views here.
from .models import Week


def index(request):
    weeks = Week.objects.all()
    context = {
        'weeks': weeks
    }
    return render(request, 'routing/index.html', context)
