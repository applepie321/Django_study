from django.shortcuts import render, redirect

def feeds(request):
    
    #user = request.user
    #is_authenticated = user.is_authenticated
    
    if not request.user.is_authenticated:
        return redirect("/users/login/")
    
    return render(request, "posts/feeds.html")
