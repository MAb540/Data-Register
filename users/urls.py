from django.urls import path
from . import views


urlpatterns = [
    path('',views.Home,name='home'),
    path('register/',views.Register,name='register')
]