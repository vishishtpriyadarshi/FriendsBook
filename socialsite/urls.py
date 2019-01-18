from django.urls import path
from .import views

urlpatterns = [
    path('', views.home , name='socialsite-home'),
    path('about/',views.about,name='socialsite-about'),
    path('profile/',views.profile,name = 'socialsite-profile')
]