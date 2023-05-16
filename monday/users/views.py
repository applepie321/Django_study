from django.shortcuts import render, redirect
from users.forms import LoginForm

def login_view(request): 
    if request.user.is_authenticated:
        return redirect("/posts/feeds")
    
    form = LoginForm()
    context = {
        "form": form,
    }
    
    return render(request, "users/login.html", context)