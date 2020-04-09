from django.contrib import admin
from django.urls import path, include
from . import views
from personal import urls

app_name = 'personal'

urlpatterns = [
    path('resume/' , views.Resume.as_view() , name ='resume'),
    path('projects/' , views.Projects.as_view() , name = 'projects'),
    path('about_me/' , views.About.as_view() , name = 'about')
]
