from django.contrib import admin
from django.urls import path,include
from .views import signup,login_page,logout_page

app_name="users"

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
]