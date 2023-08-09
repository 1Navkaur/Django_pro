from django.contrib import admin
from django.urls import path
from app_1 import views as main_view #we can import from other directory

urlpatterns = [
    path('',main_view.main_view),
    path('Home/', main_view.main_menu),
    path('contact/', main_view.main_contact),
    
]
