"""
URL configuration for lab1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import ADD, Del_Std, MyLog, Update, home, contact, about,  signup, welcome,My_logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='welcome'),
    path('home/', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('Del_Std/<int:id>', Del_Std, name='Del_Std'),
    path('Update/<int:id>', Update, name='Update'),
    path('create/',ADD,name="create"),
    path('signup/', signup, name='signup'),
    path('login/', MyLog, name='login'),
    path('logout/', My_logout, name='logout'),
]
