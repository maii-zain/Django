from django.http import HttpResponse
from django.shortcuts import redirect, render

from app.models import Person, Student


def home(request):
    # return render(request, 's1/home.html')
    students=Student.objects.all
    context={}
    context['students']=students
    return render(request, 's1/home.html',context)

def Del_Std(request,id):
    Student.objects.get(id=id).delete()
    return redirect(home)


def Update(request, id):
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
    if request.method == 'POST':
        st_name = request.POST.get('st_name')
        nd_name = request.POST.get('nd_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        Person.objects.create(st_name=st_name, nd_name=nd_name, email=email, password=password)
        return redirect('login')  
    return render(request, 's1/signup.html')
 
from django.shortcuts import render, redirect
from .models import Person

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not email or not password: 
            error_message = "Please fill in all fields."
            return render(request, 's1/login.html', {'error_message': error_message})
        
        user = Person.objects.filter(email=email, password=password).first()
        if user:
            return redirect('home')
        else:
            error_message = "Invalid email or password. Please try again."
            return render(request, 's1/login.html', {'error_message': error_message})
    else:
        return render(request, 's1/login.html')
    
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
