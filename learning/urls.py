from django.urls import path
from . import views

urlpatterns = [

    path('', views.register, name='register'),

    path('login/', views.user_login, name='login'),

    path('home/', views.home, name='home'),

    path('logout/', views.user_logout, name='logout'),

    path(
        'python/',
        views.python_course,
        name='python'
    ),
    
]