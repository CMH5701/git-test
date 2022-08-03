from multiprocessing import AuthenticationError
from django.shortcuts import render ,redirect
from django.contrib import auth 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile 
import djapp.views , account.views
# Create your views here.
def signup(request):
    if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if request.POST["password1"] == request.POST["password2"]:
                    user = User.objects.create_user(
                    username = request.POST["username"],
                    password = request.POST["password1"]
                    )
                    nickname = request.POST["nickname"],
                    email = request.POST["email"],
                    phone_num = request.POST["phone_num"],
                    age = request.POST["age"]
                    profile = Profile(user=user, nickname=nickname, email=email, phone_num=phone_num , age=age )
                    profile.save()
                    auth.login(request, user)
                    return redirect(request,'index.html')
            else:
            
                    return render(request, 'signup.html' , {'form':form})
    else:        
        form = UserCreationForm()
        return render(request, 'signup.html' , {'form':form})

def login(request):
    if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                    user = form.get_user()
                    auth.login(request, user)
                    return render(request,'index.html')
            else:
            
                    return render(request, 'login.html' , {'form':form})
    else:        
        form = AuthenticationForm()
        return render(request, 'login.html' , {'form':form})
def logout(request) :
    auth.logout(request)
    return redirect('index')