from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from courses.forms.registration_form import RegistrationForm
from courses.forms.login_form import LoginForm
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


class SignupView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, "courses/signup.html", {"form": form})  # Correct template

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "User created successfully!")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
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
    
def signout(self):
   logout(self.reuest)
   return redirect('home')
       