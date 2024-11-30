
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Administración de Django
    path('', include('myapp.urls')), # Incluye las URLs de myapp
]

