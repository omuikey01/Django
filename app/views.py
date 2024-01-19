import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import StudentFormRegistration, LoginForm, StudentQueryForm
from .models import StudentModelRegistration, StudentQuery
# Create your views here.

def homepage(request) :
    try:
        user_name = request.session['NAME']
        return render(request, "app1/index.html", {"name" : user_name, "btn" : ""})
    except :
        return render(request, "app1/index.html", {"btn" : "RLol"})

def aboutpage(request) :
    try:
        user_name = request.session['NAME']
        return render(request, "app1/about.html", {"name" : user_name, "btn" : "" })
    except :
        return render(request, "app1/about.html", {"btn" : "RLol"})

    
       
def servicepage(request) :
    try :
        user_name = request.session['NAME']
        return render(request, "app1/service.html", {"name" : user_name, "btn" : ""})
    except :
        return render(request, "app1/service.html", {"btn" : "RLol"})
    
 
def contactpage(request) :
    try:
        user_name = request.session['NAME']
        return render(request, "app1/contact.html", {"name" : user_name, "btn" : "" })
    except:
        return render(request, "app1/contact.html", {"btn" : "RLol"})
    
def registerpage(request) :
    form = {}
    form["key"] = StudentFormRegistration
    return render(request, "app1/registration.html", {"formdata" : form, "btn" : "RLol"})

def loginpage(request) :
    form = {}
    form['key'] = LoginForm
    return render(request, "app1/login.html", {"formdata" : form, "btn" : "RLol"})

def logoutpage(request) :
    request.session.flush()
    return render(request, "app1/index.html", {"btn" : "RLol"})
   

def registerdatapage(request) :
    if request.POST :
        print("Inside")
        name = request.POST['Name']
        email = request.POST['Email']
        contact = request.POST['Phone']
        pass1 = request.POST['Password']
        cpass2 = request.POST['Confirm_Password']

        try :
            user = StudentModelRegistration.objects.get(Email = email)
            form = {}
            form["key"] = StudentFormRegistration
            return render(request, "app1/registration.html",  {"formdata" : form, "data" : "Email Already Exists","btn" : "RLol"})
        except :
            form = {}
            form["key"] = LoginForm
            StudentModelRegistration.objects.create(Name  = name,
                                                Phone = contact,
                                                Email = email,
                                                Password = pass1,
                                                Confirm_Password = cpass2)
            return render(request, "app1/login.html", {"formdata" : form,"btn" : "RLol"})
    else :
        print("Outside")
    return render (request, "app1/index.html",{"btn" : "RLol"})


def logindatapage(request):
    if request.POST:
        email = request.POST['Email']
        passw = request.POST['Password']
        try :
            user = StudentModelRegistration.objects.get(Email = email)
            if user.Password == passw:                
                user_name = user.Name
                request.session['NAME'] = user_name
                request.session['EMAIL'] = user.Email
                form = {}
                form['key'] = StudentQueryForm


                return render(request, "app1/dashboard.html", {"formdata" : form, "name" : user_name, "mail" : email, "btn" : ""})
                
            else :
                form = {}
                form['key'] = LoginForm
                return render(request, "app1/login.html", {"data" : "Invalid Password ", "formdata" : form,"btn" : "RLol"})
        except :
            form = {}
            form['key'] = LoginForm
            return render(request, "app1/login.html", {"data" : "username not match","btn" : "RLol", "formdata" : form})
    else :
        print("Data need in Post Method")
    return render(request, "app1/index.html", {"btn" : "RLol"})


def dashpage(request):
    form = {}
    form['key'] = StudentQueryForm
    user_name = request.session['NAME']
    user_email = request.session['EMAIL']
    user = StudentModelRegistration.objects.get(Email = user_email)
    email = user.Email
    return render(request, "app1/dashboard.html", {"formdata" : form, "name" : user_name, "mail" : email, "btn" : ""})



def querydatapage(request):
    if request.POST:
        email = request.POST['Query_Email']
        sub = request.POST['Query_Subject']
        query = request.POST['Query']
        userMail = request.POST['qsubmitbtn']
        Current_Data = datetime.datetime.now()
        if email == userMail:
            StudentQuery.objects.create(Query_Email = email,
                                            Query_Sub = sub,
                                            QueryDate = Current_Data,
                                            Query_Query = query)
            return redirect("/dash")
        else :
            form = {}
            form['key'] = StudentQueryForm 
            user_name = request.session['NAME']
            return render(request, "app1/dashboard.html", {"formdata" : form, "name" : user_name, "mail" : email, "btn" : "", "msg" : "Account Email and Provided Email Should be match"})
        
def shawtabledatabtnpage(request):
    global tabledata
    if request.POST:
        email = request.POST['btnemail']
        allData = StudentQuery.objects.all().filter(Query_Email = email)
        form = {}
        form['key'] = StudentQueryForm        
        user_name = request.session['NAME']

        return render(request, "app1/dashboard.html", {"formdata" : form, "name" : user_name, "mail" : email, "btn" : "", "tabledata" :allData})
    else :
        pass


def EditDeleteDatapage(request):
    if request.POST:
        try:
            print("EDIT ID =============== ", editId)
            editId = request.POST['editbtn']
            form = {}
            form['key'] = StudentQueryForm
            print("********************KEYS****************")
            for i in form.keys:
                print(i)
            # print(form.keys)
            return HttpResponse("EDIT")
        
        except :
            print("DELETE ID =============== ", deleteId)
            deleteId = request.POST['deletebtn']
            StudentQuery.objects.all().filter(id = deleteId).delete()
            
            user_email = request.session['EMAIL']
            user_name = request.session['NAME']
            allData = StudentQuery.objects.all().filter(Query_Email = user_email)
            form = {}
            form['key'] = StudentQueryForm
            return render(request, "app1/dashboard.html", {"formdata" : form, "name" : user_name, "mail" : user_email, "btn" : "", "tabledata" :allData})