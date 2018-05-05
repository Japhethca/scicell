from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User


# Create your views here.
def admin_index(request):
    print(request.GET, '<><><><><><>')
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request, 'my_admin/admin-base-layout.html', {'user': request.user})
    return HttpResponseRedirect('login')


def admin_login(request):
    is_authenticated = None

    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password'],
            )

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/admin')
        else:
            is_authenticated = False
    return render(request, 'my_admin/login.html', {'is_authenticated': is_authenticated})

def admin_logout(request):
    logout(request)
    return HttpResponseRedirect('login')
