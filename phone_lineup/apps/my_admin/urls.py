from django.urls import path
from . import views


urlpatterns = [
    path('', views.admin_index, name='admin'),
    path('login', views.admin_login, name='admin-login'),
    path('logout', views.admin_logout, name='admin-logout'),
]
