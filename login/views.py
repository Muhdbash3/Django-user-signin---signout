from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def home(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if User.objects.filter(username=username):
            messages.error(request, "Username already taken! please change ")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered! please change ")
            return redirect('home')

        if User.objects.filter(username=username):
            messages.error(request, "Username already taken! please change ")
            return redirect('home')

        if len(username) > 10:
            messages.error(request, "uUsername must not be more than 10 characters")

        if pass1 != pass2:
            messages.error(request, 'passwords does not match!')

        if not username.isalnum():
            messages.error(request, "Username should be Alpha-numeric")
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Congrats Your Account has been successfully created.")

        return redirect('signin')

    return render(request, 'signup.html')


def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "index.html", {'fname': fname})

        else:
            messages.error(request, "Bad credentials")
            return redirect('home')

    return render(request, 'signin.html')


def signout(request):
    logout(request)
    messages.success(request, 'Logout successfully')
    return redirect('home')
