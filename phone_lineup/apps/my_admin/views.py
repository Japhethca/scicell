from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.contrib.auth.models import User


# Create your views here.
def admin_index(request):
    return render(request, 'my_admin/index.html')

def create_user(request):
    pass
