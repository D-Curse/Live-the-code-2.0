from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import login
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError

# Create your views here.

@login_required(login_url='signup/')
def home(request):
    return render(request, 'home.html')

def addData(request):
    return render(request, 'addData.html')

def signup(request):
    if 'submit_signup' in request.POST:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            cpassword = request.POST.get('cpassword')
            
            errors = {}
            
            if User.objects.filter(username=username).exists():
                errors['existing_user'] = True
            if cpassword != password:
                errors['errors_password'] = True
            try:
                validate_password(password)
            except ValidationError as error:
                errors['error_pass_validation'] = error
                
            if errors:
                errors.update({'error': True, 'username': username, 'password': password})
                return render(request, "signup.html", errors)
            else:
                myuser = User.objects.create_user(username=username, password=password)
                myuser.save()
            
                return redirect('signup')
        
    if 'submit_login' in request.POST:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            
            print(username)
            print(password)
            
            user = authenticate(username=username, password=password)
            
            print('before if')
            if user is not None:
                print(user)
                login(request, user)
                return redirect('home')
            else:
                return render(request, "signup.html", {'error_invalid':True})
            
        
    
    return render(request, 'signup.html')
