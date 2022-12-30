from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from app1.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request,'index.html')
    # return HttpResponse("hey bro cool down")
    messages.success(request,'this is test message')

def about(request):
    return render(request,'about.html')
    # return HttpResponse("hey bro cool down about")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email=request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email = email,desc = desc,)
        contact.save()
        messages.success(request, 'Your message has been sent')
    return render(request,'contact.html')
    # return HttpResponse("hey bro cool down contact")

def services(request):
    return render(request,'services.html')
    # return HttpResponse("hey bro cool down services")

# def front(request):
    # return render(request,'front.html')


def signup(request):
    
    if request.method == "POST":
        email1 = request.POST['email1']
        passWord = request.POST['passWord']
        ursername = request.POST['Ursername']
        fname = request.POST['fname']
        lname = request.POST['lname']
        
        if User.objects.filter(username = ursername).first():
            messages.error(request, "This username is already taken")
            return redirect('/')


        myuser = User.objects.create_user(ursername,email1,passWord,)
        
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"your account succesfully signup")
        return redirect('/')
        

    else:
        return HttpResponse("404 not found")    
    

def handlelogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        passWord1 = request.POST['passWord1']
       
        user = authenticate(username = loginusername, password = passWord1)
        if user is not None:
            login(request,user)
            messages.success(request,"you are loged in succesfully")
            return redirect("/about")
        else:
            messages.error(request,"Invalid username & pass") 
            return redirect("/")   


    return HttpResponse('404 - not found')



    # return HttpResponse("hello in")

def handlelogout(request):
    logout(request)
    messages.success(request,"you are logged out succesfully")
    return redirect("/")


    # return HttpResponse("handlelogout")