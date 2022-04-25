from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home-page'), #ourdomain.com/challenges/
    path('<int:month>/',views.index_num,name='index_num-page'), # ourdomain.com/challenges/integer
    path('<str:month>/',views.index,name='index-page'), # ourdomain.com/challenges/month
]