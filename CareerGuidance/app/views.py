from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app.models import Course, Details, EduDetails
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import login
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError

# Create your views here.

@login_required(login_url='signup/')
def home(request):
    return render(request, 'home.html')

def courseDetails(request):
    main_context = Details.objects.get(pk=1)
    print(main_context.main_head)
    print(main_context)
    edu_context = EduDetails.objects.all()
    return render(request, 'details.html', {'main_context': main_context, 'edu_context': edu_context})

def dataAdminInfo(request):
    main_head = None
    if 'submit-course-info' in request.POST:
        if request.method == 'POST':
            main_head = request.POST.get('main_head')
            image = request.FILES.get('image')
            career_head = request.POST.get('career_head')
            career_para = request.POST.get('career_para')
            
    
            detailsCourse = Details(
                main_head=main_head, 
                image=image,
                about_career_head=career_head,
                about_career_para=career_para,
            )
            detailsCourse.save()
            
            request.session['main_context'] = detailsCourse
            
            return redirect('addInfo')
        
    if 'submit-edu-info' in request.POST:
        if request.method == 'POST':
            main_head1 = request.POST.get('main_head')
            edu_stream = request.POST.get('edu_stream')
            edu_gradution = request.POST.get('edu_gradution')
            edu_after_grad = request.POST.get('edu_after_grad')
            edu_post_grad = request.POST.get('edu_post_grad')
            
            detailsEdu = EduDetails(
                main_head=main_head1, 
                edu_stream=edu_stream,
                edu_graduation=edu_gradution,
                edu_after_grad=edu_after_grad,
                edu_post_grad=edu_post_grad,
            )
            detailsEdu.save()
            
            request.session['edu_context'] = detailsEdu
            
            return redirect('addInfo')
    return render(request, 'details-template.html')



def dataAdmin(request):
    if 'submit-course-info' in request.POST:
        if 'field_name' in request.POST and 'course' in request.POST:
            field_name = request.POST['field_name']
            branch = request.POST['course']

            info = Course(field_name=field_name, branch=branch)
            info.save()

        return redirect('add')
    return render(request, 'data-admin.html')

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