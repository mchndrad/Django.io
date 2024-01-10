from unicodedata import name
from django.urls import path
from django.contrib import admin
from . import views
from kerangka import views

urlpatterns = [
    path('home.html',views.home,name='home'),
    path('profile/home.html',views.home),
    path('viewbndung.html',views.viewbndung),
    path('viewbali.html',views.viewbali),
    path('viewcrbon.html',views.viewcrbon),
    path('viewjkrta.html',views.viewjkrta),
    path('viewjogja.html',views.viewjogja),
    path('viewmalang.html',views.viewmalang),
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('signup/',views.signup, name='signup'),
    path('profile/',views.profile, name='profile'),
    path('booking.html',views.booking, name='booking'),
    path('profile/viewbali.html',views.viewbali, name='viewbali'),
    path('profile/viewbndung.html',views.viewbndung, name='viewbndung'),
    path('profile/viewcrbon.html',views.viewcrbon, name='viewcrbon'),
    path('profile/viewjkrta.html',views.viewjkrta, name='viewjkrta'),
    path('profile/viewjogja.html',views.viewjogja, name='viewjogja'),
    path('profile/viewmalang.html',views.viewmalang, name='viewmalang'),
    path('profile/booking.html',views.booking, name='booking'),
    
]
