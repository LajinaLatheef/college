from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from.models import Data


# Create your views here.

def demo(request):
    return render(request,"index.html")

def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return render(request,'new.html')
        else:
            messages.info(request,"Invalid credentials")
            return redirect("login")
    return render(request,"login.html")


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect ("register")
            else:
                user=User.objects.create_user(username=username,password=password)


                user.save()
                return redirect('collegeapp:login')
            # print("user created")
        else:
            messages.info(request,"password not matching")
            return redirect("collegeapp:register")

        return redirect('/')

    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def form(request):
    if request.method=='POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        phonenumber = request.POST['phonenumber']
        mailid = request.POST['mailid']
        address = request.POST['address']
        department = request.POST.get('department',None)
        courses = request.POST.get('courses',None)
        purpose = request.POST.get('purpose',None)
        materials = request.POST.get('materials',False)

        data=Data(name=name,dob=dob,age=age,phonenumber=phonenumber,mailid=mailid,address=address)

        data.save()
        messages.success(request,"Successfully submitted")

    return render(request,'form.html')











