
from django.contrib import admin
from django.urls import path
from quickapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('gallery/', views.gallery),
]
