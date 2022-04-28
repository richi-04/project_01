from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



# Create your views here.
def registerForm(request):
    if request.method == 'POST':
        username = request.POST["uname"]
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", username)
        email = request.POST["email"]
        print("🚀 ~ file: views.py ~ line 12 ~ email", email)
        phone = request.POST["phone"]
        print("🚀 ~ file: views.py ~ line 14 ~ phone", phone)
        gender = request.POST["gender"]
        print("🚀 ~ file: views.py ~ line 16 ~ gender", gender)
        password = request.POST["password"]
        print("🚀 ~ file: views.py ~ line 18 ~ password", password)
        hobby_data = request.POST.getlist('hobby[]')
        print("🚀 ~ file: views.py ~ line 20 ~ hobby", hobby_data)
        x = ','.join(hobby_data)
        hobby_data = str(x)

        profiledata = Profile(uname=username,email=email,phone=phone,gender=gender,password=password,hobby=hobby_data)
        profiledata.save()
             

    return render(request, 'register.html')




def loginForm(request): 
    username = request.POST.get('uname')
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", username)
    password = request.POST.get('password')
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", password)
    user = authenticate(username='admin', password='admin')
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", user)
    if user is not None:
      login(request, user)
      return redirect("home")
    else:
        return render(request, "login.html")


def home(request):
    return render(request, 'home.html')