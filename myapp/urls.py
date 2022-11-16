from django.urls import path
from myapp.views import *


urlpatterns = [
    path('',index,name="index"),
    path('login/',login_user,name="login"),
    path('signup',signup,name="signup"),
    path('logout',logout_user,name="logout"),
    path('profile',user_profile,name="profile"),
    ]
