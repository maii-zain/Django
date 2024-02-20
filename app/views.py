from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from app.models import Person, Student

# @login_required
def home(request):
    # return render(request, 's1/home.html')
    if request.session.get('email'):
         students=Student.objects.all
         context={}
         context['students']=students
        #  request.session['students']=students
         return render(request, 's1/home.html',context)
    else:
        return redirect('login')

def Del_Std(request,id):
    Student.objects.get(id=id).delete()
    return redirect(home)


def Update(request, id):
    # if request.method == 'GET':
    #     return render(request, 's1/home.html')

    student = Student.objects.get(id=id)
    context = {'student': student}

    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['age']
        
        student.f_name = fname
        student.l_name = lname
        student.age = age
        student.save()
        return redirect('home')

    return render(request, 's1/update.html', context)

def ADD(request):
    if request.method == 'GET':
        return render(request, 's1/add.html')

    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        age = request.POST.get('age')
        
        Student.objects.create(f_name=f_name, l_name=l_name, age=age)

        return redirect('home')

def signup(request):
    if request.method == 'GET':
        return render(request, 's1/signup.html')
    elif request.method == 'POST':
        st_name = request.POST.get('st_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check if the email already exists in the User model
        if User.objects.filter(email=email).exists():
            error_message = 'Email already exists. Please choose a different one.'
            return render(request, 's1/signup.html', {'error_message': error_message})
        
        # Create the user if the email doesn't exist
        user = User.objects.create_user(username=st_name, email=email, password=password)
        return redirect('login')


def MyLog(request):
    if request.method == 'GET':
        return render(request, 's1/login.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check if the email exists in the User model
        user = User.objects.filter(email=email).first()
        
        if user:
            # Authenticate user
            auth = authenticate(request, username=user.username, password=password)
            if auth:
                # Login user
                login(request, auth)
                # Set session key
                request.session['email'] = email
                # Redirect to home page
                return redirect('home')
            else:
                invalid_message = "Invalid email or password. Please try again."
                return render(request, 's1/login.html', {'error_message': invalid_message})
        else:
            not_exist_msg = "Email is not registered."
            return render(request, 's1/login.html', {'error_message': not_exist_msg})
def My_logout(request):
    request.session.clear()
    logout(request)
    return redirect(MyLog)                          
    #         users=User.objects.all()
    #         print(users[0].password)
            
    #     else:
    #         error_message = "Invalid email or password. Please try again."
    #         return render(request, 's1/login.html', {'error_message': error_message})
    # else:
    #     return render(request, 's1/login.html')
    
def contact(request):
    return render(request, 's1/contact.html')

def about(request):
    return render(request, 's1/about.html')
def welcome(request):
    return render(request, 's1/welcome.html')
# def Show_student(request):
#     students=Student.objects.all
#     context={}
#     context['students']=students
#     return render(request, 's1/home.html',context)
    
#     print(students)
#     return HttpResponse(f'{request}')
