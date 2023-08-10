from django.contrib import admin
from django.urls import path
from app_1 import views as main_view #we can import from other directory

urlpatterns = [
    path('',main_view.main_view),
    path('Home/', main_view.main_menu),
    path('contact/', main_view.main_contact),
     path('monday/', main_view.main_mon),
      path('tuesday/', main_view.main_tue),
       path('wednesday/', main_view.main_wed),
        path('thursday/', main_view.main_thur),
         path('friday/', main_view.main_fri), 
          path('saturday/', main_view.main_sat),
           path('sunday/', main_view.main_sun),
           
    
]
