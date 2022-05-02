from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages




# Create your views here.
def registerForm(request):
    if request.method == 'POST':
        username = request.POST["username"]
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", username)
        email = request.POST["email"]
        print("🚀 ~ file: views.py ~ line 12 ~ email", email)
        phone = request.POST["phone"]
        print("🚀 ~ file: views.py ~ line 14 ~ phone", phone)
        gender = request.POST["gender"]
        print("🚀 ~ file: views.py ~ line 16 ~ gender", gender)
        password = request.POST["password"]
        print("🚀 ~ file: views.py ~ line 18 ~ password", password)
        password2 = request.POST["password2"]
        print("🚀 ~ file: views.py ~ line 24 ~ password2", password2)
        hobby_data = request.POST.getlist('hobby[]')
        print("🚀 ~ file: views.py ~ line 20 ~ hobby", hobby_data)
        x = ','.join(hobby_data)
        hobby_data = str(x)

        if len(username)<5 or len(phone)<10 or (password!=password2):
            messages.error, "Please fill the form correctly"
            return HttpResponse("fill the form again")
          
        else:
            data_save = Profile(username=username,email=email,phone=phone,gender=gender,password=password,password2=password2,hobby=hobby_data)
            data_save.save()
            return redirect('login')

    else:        
        return render(request, 'register.html')




def loginForm(request): 
    username = request.POST.get('username')
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", username)
    password = request.POST.get('password')
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", password)
    user = authenticate(username='login01', password=password)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", user)
    if user is not None:
      login(request, user)
      return redirect("home")
    else:
        return render(request, "login.html")


def home(request):
    return render(request, 'home.html')