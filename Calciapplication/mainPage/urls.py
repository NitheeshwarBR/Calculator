from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('home/',views.home,name="home"),
    path('login/',views.home,name="home"),
    path('signup/',views.signup,name="signup"),
    path('signup/login/',views.backlogin,name="backlogin"),
]