from django.urls import path
from . import views


urlpatterns = [
    path('', views.admin_index, name='admin'),
    path('create', views.create_user, name='create_user'),
]
