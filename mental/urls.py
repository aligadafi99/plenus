from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name="home"),
    path('groups/', views.group , name="groups"),
    path('homepage/', views.homepage , name="homepage"),
    path('room/<str:pk>/', views.room , name="room"),
   
    path('sasa/', views.sasa , name="sasa"),
    path('topics/', views.topicsPage, name="topics"),
    
    path('createroom/', views.createRoom , name="createroom"),
    path('signUp',views.signUp,name = 'signUp'),
    path('login',views.login,name = 'login'),
    path('signout',views.signout,name = 'signout'),
   
]