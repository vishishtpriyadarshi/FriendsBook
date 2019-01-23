from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home , name='socialsite-home'),
    path('about/',views.about,name='socialsite-about'),
    path('profile/',views.profile,name = 'socialsite-profile'),
    
]

if settings.DEBUG :
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)