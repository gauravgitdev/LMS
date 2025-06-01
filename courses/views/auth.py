from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from courses.forms.registration_form import RegistrationForm
from courses.forms.login_form import LoginForm
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate, login



class SignupView(View):
    def get(self,request):
        form = RegistrationForm()
        return render(request, "courses/login.html" , {"form": form})
        form = RegistrationForm()


    def post(self,request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
         messages.success(request, "User created successfully!")
        user = form.save()
        if user is not None:
            return redirect('login')
            
        else:
         return render(request, "courses/signup.html", {"form": form})
   




   



class Loginview(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "courses/login.html", {'form': form})

    def post(self, request):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect('home')
        messages.error(request, "Invalid username or password")
        return render(request, "courses/login.html", {'form': form})