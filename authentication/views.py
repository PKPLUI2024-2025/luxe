from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage:home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@csrf_protect  # Tambahkan untuk memastikan CSRF Protection berjalan
def user_login(request):
    if request.method == 'POST':
        csrf_token_post = request.POST.get('csrfmiddlewaretoken')
        csrf_token_cookie = request.COOKIES.get('csrftoken')

        print("Request CSRF Token:", csrf_token_post)
        print("Cookie CSRF Token:", csrf_token_cookie)

        if not csrf_token_post or not csrf_token_cookie:
            return JsonResponse({"error": "CSRF token missing"}, status=403)

        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage:home')  # Redirect jika login berhasil
        
        return render(request, 'login.html', {'form': form, "error": "Invalid login credentials"})  # Jika form tidak valid, kembali ke login page
    
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')
