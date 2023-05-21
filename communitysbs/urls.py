from django.contrib import admin
from django.urls import path, include

# Connecting the admin file to the backend platform and the app folder
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
]