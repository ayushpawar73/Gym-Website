

import email
from django.shortcuts import redirect, render
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from pawar2.models import feedback
def index(request):
      
      return render(request,'index.html')
  
def price2(request):
    data=userdata.objects.all()
    oj2={"data":data}
    print(data)
    print(data)
    print(data)
    print(data)
    return render(request,'pricing.html',oj2)

def about(request):
 return render(request,'about.html')
 
def userinf(request):
     data2=userdata.objects.all()
     d2={"data2":data2}
     print("Prajjwal")
     print(data2)
           
     return render(request,'userinfo.html',d2)
 
def index1(request):
   if request.method =='POST':
       
       unm=request.POST['username']
       psw=request.POST['password']
       eml=request.POST['email12']
       user=User.objects.create(username=unm,password=psw,email=eml)
       user.save()
       
   return render(request,'Login.html')
def services(request):
 return render(request,'Services.html')

#def feedback(request):
 #return render(request,'Feedback.html')

def Feedback(request):
       data = feedback.objects.all()
       print(data)
       if request.method=="POST":
        u=request.POST["fname"]
        v=request.POST["lname"]
        w=request.POST["mailid"]
        x=request.POST["country"]
        y=request.POST["feedback"]
       
        feedback.objects.create(firstname=u,lastname=v,mail_id=w,country=x,feedback=y)
       return render(request,'Feedback.html')





def form(request):
   if request.method == 'POST':
      username=request.POST['username1']
      password=request.POST['password1']
      user=authenticate(request,username=username,password=password)
      print(user)
      try:
         if user.is_staff:
            auth_login(request,user)
            data=feedback.objects.all()
            d={"data":data}
            print("Prajjwal")
            print("Prajjwal")
            print("Prajjwal")
            print("Prajjwal")
            print(data)
            return render(request,"adredirect.html",d)
         else :
          user is not None
          auth_login(request,user)
        #   if request.method=="POST":
        #    name=request.POST["formf"]
        #    lname=request.POST["forml"]
        #    gender=request.POST["formg"]
        #    lbs=request.POST["formlbs"]
        #    weight=request.POST["formdesired_weight"]
        #    height=request.POST["height"]
        #    address=request.POST["home_address"]
        #    city=request.POST["city"]
        #    state=request.POST["state"]
        #    zipcode=request.POST["code"]
        #    country=request.POST["country"]
        #    mailid=request.POST["email"]
        #    phoneno=request.POST["phone"]
        #    plan=request.POST["plan"] 
        #    print("this is pen")
        #    print("this is pen")
        #    print("this is pen")
        #    print(height,city,weight,state,plan,mailid)
        #    print("this is pen")
        #    print("this is pen")
        #    print("this is pen")

        #    userdata.objects.create(firstname=name,lastname=lname,gender=gender,lbs=lbs,weight=weight,height=height,address=address,city=city,state=state,zipcode=zipcode,country=country,email=mailid,phoneno=phoneno,plan=plan)
          return render(request,"afterlogin.html")
         #return redirect('/form1')
         #else:
         #return redirect('/')
         # return render(request,"index.html")
      except Exception as ep: 
         print("Hello ")
         print("Hello ")
         print("Hello ")
         print(ep)
         return render(request,"blank.html")
   return render(request,"Services.html")
def bodybuild(request):
    return render(request,"profbody.html")
def crossfit(request):
    return render(request,"crossfit.html")

def certify(request): 
    data2=participantname.objects.all()
    print("printing fetched datt")
    print("printing fetched datt")
    print("printing fetched datt")
   
    print("Printing Certificate")
    if request.method == "POST":
         print("Prajjwal")
         print("ayush")
         print("Prajjwal")
         print("ayush")
         parname=request.POST["certificatename"]
         try:
            print("changing data")
            print(parname)
            data=data=participantname.objects.all()
            data.pname=parname
            data.save()
         except Exception as ep:
          print(ep)
          participantname.objects.create(pname=parname)
         print(parname)
    return render(request,"certificatepg.html")
    
          
          
     

def functional(request):
    return render(request,"functional.html")
def fittraining(request):
    return render(request,"fitnesstraining.html")
def yoga(request):
    return render(request,"yoga.html")
def zumba(request):
    return render(request,"zumba.html")
def fitnesstrain(request):
    return render(request,"performance.html")
def cardio(request):
    return render(request,"cardio.html")
def adredirect(request):
   data = feedback.objects.all()
   print(data)
   return render(request,"adredirect.html")

def gal(request):
    return render(request,"gallery.html")
def che(request):
    return render(request,"new.html")

def cirgen(request):
    print("cirgen")
    print("inside cirgen")
    print("inside cirgen")
    if request.method == "POST":
         print("Prajjwal")
         print("ayush")
         print("Prajjwal")
         print("ayush")
         parname=request.POST["certificatename"]
         participantname.objects.create(pname=parname)
         print(parname)
    print("objectcal;ling")
    print("objectcal;ling")
    print("objectcal;ling")
    print("objectcal;ling")
    print("objectcal;ling")
    pnam=request.user
    print(pnam)
    data=participantname.objects.all()
    print(data)
    d1={"data":data}
    print("Prajjwal")
    print("Prajjwal")
    print("Prajjwal")
    print("Prajjwal")
    return render(request,"maincertificate.html",d1)

def newnav(request):
    return render(request,"navigation.html")

def prajjwal1(request):
     print("this is pen")
     print("this is pen")
     print("this is pen")
     print("this is pen")
     if request.method == "POST":
        print("printing post method")
        name=request.POST["formf"]
        lname=request.POST["forml"]
        gen=request.POST["ayus"]
        # gender=request.POST["formg"]
        lbs=request.POST["formlbs"]
        weight=request.POST["formdesired_weight"]
        height=request.POST["height"]
        address=request.POST["home_address"]
        city=request.POST["city"]
        state=request.POST["state"]
        zipcode=request.POST["code"]
        country=request.POST["country"]
        mailid=request.POST["email"]
        phoneno=request.POST["phone"]
        plan=request.POST["plan"] 
        print("this is pen")
        print("this is pen")
        print("this is pen")
        print(height,city,weight,state,plan,mailid)
        print("this is pen")
        print("this is pen")
        print("this is pen")
        inf=userdata.objects.create(firstname=name,lastname=lname,gender=gen,lbs=lbs,weight=weight,height=height,address=address,city=city,state=state,zipcode=zipcode,country=country,email=mailid,phoneno=phoneno,plan=plan)
        inf.save()
        return render(request,"afterlogin.html")
   