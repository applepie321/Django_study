from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from users.forms import LoginForm
from users.forms import SignupForm
from users.models import User

def login_view(request): 
    if request.user.is_authenticated:
        return redirect("/posts/feeds/")
    
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            
            if user:
                login(request, user)
                return redirect("/posts/feeds/")
            else:
                form.add_error(None, "자격증명 에러")
            
            
        context = {"form": form}
        return render(request, "users/login.html", context)
    else: 
        form = LoginForm()
        context = {"form": form}    
        return render(request, "users/login.html", context)
    
    
def logout_view(request):
    logout(request)
    return redirect("/users/login")

def signup(request):
    if request.method == "POST":
        form = SignupForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            
            
            if password1 != password2:
                form.add_error("pssword2", "비밀번호와 비밀번호 확인란의 값이 다릅니다.")
                
            if User.objects.filter(username=username).exists():
                form.add_error("username", "이미 사용중인 사용자명입니다.")
                
            if form.errors:
                context = {"form": form}
                return render(request, "users/signup.html", context)
            
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password1,
                )
                login(request, user)
                return redirect("/posts/feeds")
            
    else:
        form = SignupForm()
        context = {"form": form}
        return render(request, "users/signup.html", context)
            
    
    
    # form = SignupForm()
    # context = {"form": form}
    # return render(request, "users/signup.html")