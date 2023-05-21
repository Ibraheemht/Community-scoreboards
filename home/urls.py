from django.contrib import admin
from django.urls import path, include
from home import views

# Titles for the backend platform
admin.site.site_header = "Tina Admin"
admin.site.site_title = "Back-end portal"

# Linking the views.py file to this one (urls.py)
urlpatterns = [
    path('', views.home, name='home'),
    path('submit', views.submit, name='submit'),
]  