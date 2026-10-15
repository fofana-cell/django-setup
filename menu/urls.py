from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/menu/', views.menu_api, name='menu_api'),
]
