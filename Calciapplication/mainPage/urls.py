from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('signup/',views.signup,name="signup"),
    path('signup/login',views.Loginpage,name="Loginpage"),
    path('home/',views.home,name="home"),
    path('signup/signup',views.Loginpage,name="Loginpage"),
    path('signup/login/',views.home,name="home"),
    path('login/',views.home,name="home"),
    

    
]