from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('scan/', views.scan_qr, name='scan_qr'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('quienesomos/', views.quienesomos, name='quienesomos'),
]

