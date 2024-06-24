from django.urls import path
from hero.views import HeroDetail, HeroAdd

urlpatterns = [
    path('<str:id>/', HeroDetail.as_view()),
    path('', HeroAdd.as_view()),
]