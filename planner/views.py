from django.http import HttpResponse
# from django.shortcuts import render

from .models import Week
from congregation.models import Congregation

# Create your views here.


def index(request):
    weeks = [1000, 2000, 3000]
    for n in weeks:
        w = Week.objects.get_or_create(week=n)
        Week.objects.create(week=n + 1)
   # Congregation.objects.get(id=1)

    return HttpResponse(f"Hello is the planner {w[0]} {w[1]}  page")
