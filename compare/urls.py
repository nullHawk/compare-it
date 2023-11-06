from django.urls import path
from . import views

urlpatterns = [
    path('compare/', views.compare, name='compare'),
    path('', views.front_end, name="front_end")
]
