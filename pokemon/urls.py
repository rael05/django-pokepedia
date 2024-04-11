from django.urls import path
from .views import poke_list, poke_detail

urlpatterns = [
    path('', poke_list, name="index"),
    path("<int:number>/", poke_detail, name="detail"),
]