from django import forms
from django.contrib.auth import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, UserManager
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib import messages
from myapp.forms import Items, UserForm,Records
from random import randrange
from myapp.forms import Item,record
from django.conf import settings
from django.core.mail import EmailMessage,send_mail
from .models import *

# import backends.base.SessionBase

# password: lbwrvmmdwscxcgyc


# Create your views here.
# user1=""
def index(request):
    if request.method == "POST":
        uname=request.POST.get("username")
        pwd=request.POST.get("password")
        fname=request.POST.get("first_name")
        lname=request.POST.get("last_name")
        
        if User.objects.filter(username=uname).exists():
            print("Existsss")
            messages.error(
            request,
            "User already exists",
            extra_tags="alert alert-error alert-dismissible show",)
            return render(request,'index.html')

        else:
            global temp
            temp = {
            'uname' : uname,
            'pwd' : pwd,
            'fname' : fname,
            'lname' : lname,
            }        
            otp = randrange(1000,9999)
            subject = 'welcome!!'
            message = f'Hi your otp for Reset password is {otp}.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [uname, ]
            send_mail( subject, message, email_from, recipient_list )
            return render(request,'verify_otp.html',{'otp':otp})
    else:
        return render(request,'index.html')


def otp(request):
    if request.method == "POST":
        otp = request.POST['otp']
        uotp = request.POST['uotp']
        if otp == uotp:
            global temp
            user = UserForm()
            form = user.save(commit=False)
            form.username = temp["uname"]
            form.first_name = temp["fname"]
            form.last_name = temp["lname"]
            form.set_password(temp["pwd"])
            form.save()
            return render(request,'index.html')
    else:
        return render(request,'verify_otp.html')

def auth(request):
    if request.method=="POST":

        username = request.POST.get("id")
        password = request.POST.get("pwd")
        user = authenticate(username=username, password=password)
        if user:
            request.session['username']=username
            userf=User.objects.filter(username=username)
            return render(request, "dashboard.html",{'userf':userf})
        else:
            messages.error(
                request,
                "Account is invalid",
                extra_tags="alert alert-error alert-dismissible show",
            )
            return redirect("index")
    else:
        userf=User.objects.filter(username=request.session['username'])
        return render(request, "dashboard.html",{'userf':userf})

def additems(request):
    if request.method == "POST":
        print(request.POST)
        form=Items(request.POST)
        # username = request.POST.get('username')
        # form.fields['username'].choices = [(username, username)]
        if form.is_valid():
            form.save()
            messages.success(request, "Item added successfully")
            msg='*item has been added successfully !!!'
            uid=request.session['username']
            return render(request,"items.html",{'uid':uid,'msg':msg})
        else:
            print(form.errors)
            return HttpResponse("Invalid!!!!")
    else:
        uid=request.session['username']
        return render(request,"items.html",{'uid':uid})


def updateitems(request):
    uname=request.session['username']
    allIteams = Item.objects.filter(username=uname)
    context = {'items':allIteams}
    return render(request,"updateitems.html", context)

def edit(request):
    item = Item.objects.all()
    context = {
        'item' : item
    }
    return redirect(request,"updateitems.html")

def update(request):
    if request.method == "POST":
        itemname = request.POST.get('itemName')
        itemdesc = request.POST.get('itemDesc')
        sellprice = request.POST.get('sellPrice')
        quantity = request.POST.get('quantity')
        tempid = request.POST.get('id')

        item = Item.objects.get(id=tempid)
        item.itemName = itemname
        item.itemDesc = itemdesc
        item.sellPrice = sellprice
        item.quantity = quantity
        item.save()
        return redirect("updateitems")
    return HttpResponse("Error")

def delete(request):
    if request.method == "POST":
        tempid = request.POST.get('id')
        Item.objects.filter(id=tempid).delete()
        return redirect("updateitems")
    return HttpResponse("Error")

def search(request):
    if request.method=='POST':
        cate=request.POST.get('category')
        # request.session['category']=cate
        Items = Item.objects.filter(Category=cate)
        cat=Item.objects.values_list('Category',flat=True)
        cat=set(cat)
        return render(request,'search.html',{"items":Items,'category':cat,'selcat':cate,})  
    else:
        uname=request.session["username"]
        Items = Item.objects.filter(username=uname)
        cat=Item.objects.values_list('Category',flat=True)
        cat=set(cat)
        return render(request,'search.html',{"items":Items,'category':cat})

# def sell(request,id=0):
#     items=Item.objects.get(pk=id)
#     form=Items(instance=items)
#     return render(request,'search.html',{"form":form})

def sell(request):
    if request.method == "POST":
        itemname = request.POST.get('itemName')
        itemdesc = request.POST.get('itemDesc')
        sellprice = request.POST.get('sellPrice')
        quantity = request.POST.get('quantity')
        tempid = request.POST.get('id')

        item = Item.objects.get(id=tempid)
        item.itemName = itemname
        item.itemDesc = itemdesc
        item.sellPrice =  sellprice
        item.quantity = item.quantity-int(quantity)    
        item.save()
        return redirect("search")
    return HttpResponse("Error")


def addRecords(request):
    if request.method == "POST":
        print(request.POST)
        form=Records(request.POST)
        # username = request.POST.get('username')
        # form.fields['username'].choices = [(username, username)]
        if form.is_valid():
            form.save()
            return redirect("search")
        else:
            print(form.errors)
            return HttpResponse("Invalid!!!!")
    else:
        uname=request.session["username"]
        print
        records= record.objects.filter(username=uname)
        print(records)
        return render(request,'records.html',{"items":records})

def logout_view(request):
    logout(request)
    return redirect('index')



    # if not user:
    #     messages.error(
    #         request,
    #         "Account is invalid",
    #         extra_tags="alert alert-error alert-dismissible show",
    #     )
    #     return redirect("index")
    # else:
    #     return render(request, "login.html")

# def verify(request):
#     a = request.POST.get("uotp")
#     b = request.POST.get("otp")
#     user=request.POST.get("username")
#     # if a == b:
#     #     return redirect("index")
#     return HttpResponse("hello" + str(a) + str(b)+str(user))


# def emailverify(request):
#     subject = "welcome to GFG world"
#     message = f"Hi {user.username}, thank you for registering in geeksforgeeks."
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [
#         user.email,
#     ]
#     send_mail(subject, message, email_from, recipient_list)
