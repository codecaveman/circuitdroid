from django.urls import path

app_name = 'congregation'
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:congregation_id>/', views.detail, name='detail'),
]
