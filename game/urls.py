from django.urls import path

from . import views

urlpatterns = [
        path('ttt', views.form, name='form'),
        path('ttt/play/', views.game, name='game'),
        path('ttt/', views.form, name='form'),
        path('ttt/play', views.game, name='game')
]


