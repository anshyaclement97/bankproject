from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
import os
from samproject.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        a = regform(request.POST)
        if a.is_valid():
            cn = a.cleaned_data['companyname']
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            cp = a.cleaned_data['password2']
            mb = a.cleaned_data['mobile']
            ad = a.cleaned_data['address']
            if ps == cp:
                b = regmodel(companyname=cn, email=em, password=ps, mobile=mb, address=ad)
                b.save()
                return redirect(login)
            else:
                return HttpResponse("Incorrect password")
        else:
            return HttpResponse("Registration failed")
    return render(request, 'register.html')


# correct

def login(request):
    if request.method == 'POST':
        a = logform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            b = regmodel.objects.all()
            for i in b:
                cmp = i.companyname
                id = i.id

                # print(id)
                if i.email == em and i.password == ps:
                    return render(request, 'profile.html', {'cmp': cmp, 'id': id})
            else:
                return HttpResponse("Login failed")
    else:
        return render(request, 'login.html')


# def login(request):
#     if request.method == 'POST':
#         a = logform(request.POST)
#         if a.is_valid():
#             em = a.cleaned_data['email']
#             ps = a.cleaned_data['password']
#             b = regmodel.objects.all()
#             for i in b:
#                 cmp = i.companyname
#                 id = i.id
#                 ema = i.email
#                 # print(id)
#                 if i.email == em and i.password == ps:
#                     return render(request, 'profile.html', {'cmp': cmp, 'id': id,'ema':ema})
#             else:
#                 return HttpResponse("Login failed")
#     else:
#         return render(request, 'login.html')


def navbar(request):
    return render(request, 'navbar.html')


def footer(request):
    return render(request, 'footer.html')


def profile(request):
    return render(request, 'profile.html')


def testimonials(request):
    return render(request, 'testimonials.html')


def about(request):
    return render(request, 'about.html')


def terms(request):
    return render(request, 'terms.html')


def samplenavbar(request):
    return render(request, 'samplenavbar.html')


def contact(request):
    return render(request, 'contact.html')


# def sendmessage(request):
#     return render(request,'sendmessage.html')


# correct

def vaccancyupload(request, id):
    b = regmodel.objects.get(id=id)
    cm = b.companyname
    em = b.email

    if request.method == 'POST':
        a = vaccancyuploadform(request.POST)
        if a.is_valid():
            cn = a.cleaned_data['companyname']
            em = a.cleaned_data['email']
            jt = a.cleaned_data['jobtitle']
            jp = a.cleaned_data['jobtype']
            wt = a.cleaned_data['worktype']
            er = a.cleaned_data['experiencerequired']
            qr = a.cleaned_data['qualificationrequired']
            b = vaccancyuploadmodel(companyname=cn, email=em, jobtitle=jt, jobtype=jp, worktype=wt,
                                    experiencerequired=er, qualificationrequired=qr)
            b.save()
            return redirect(vaccancysuccess)
        else:
            return HttpResponse("Upload failed")
    return render(request, 'vaccancyupload.html', {'cm': cm, 'em': em})


#


# def vaccancyupload(request, id):
#     b = regmodel.objects.get(id=id)
#     cm = b.companyname
#     em = b.email
#     id = b.id
#
#     if request.method == 'POST':
#         a = vaccancyuploadform(request.POST)
#         if a.is_valid():
#             cn = a.cleaned_data['companyname']
#             em = a.cleaned_data['email']
#             jt = a.cleaned_data['jobtitle']
#             jp = a.cleaned_data['jobtype']
#             wt = a.cleaned_data['worktype']
#             er = a.cleaned_data['experiencerequired']
#             qr = a.cleaned_data['qualificationrequired']
#             b = vaccancyuploadmodel(companyname=cn, email=em, jobtitle=jt, jobtype=jp, worktype=wt,
#                                     experiencerequired=er, qualificationrequired=qr)
#             b.save()
#             return redirect(vaccancysuccess)
#         else:
#             return HttpResponse("Upload failed")
#     return render(request, 'vaccancyupload.html', {'cm': cm, 'em': em,'id':id})


def vaccancysuccess(request):
    a = vaccancyuploadmodel.objects.all()
    return render(request, 'vaccancysuccess.html', {'a': a})


# def vaccancysuccess(request,id):
#         b = regmodel.objects.get(id=id)
#         em = b.email
#         ps = b.password
#
#
#         a = vaccancyuploadmodel.objects.get(email=em,password = ps)
#         return render(request, 'vaccancysuccess.html', {'a': a})


def vaccancyedit(request, id):
    a = vaccancyuploadmodel.objects.get(id=id)
    if request.method == 'POST':
        a.companyname = request.POST.get('companyname')
        a.email = request.POST.get('email')
        a.jobtitle = request.POST.get('jobtitle')
        a.jobtype = request.POST.get('jobtype')
        a.worktype = request.POST.get('worktype')
        a.experiencerequired = request.POST.get('experiencerequired')
        a.qualificationrequired = request.POST.get('qualificationrequired')
        a.save()
        return redirect(vaccancysuccess)
    return render(request, 'vaccancyedit.html', {'a': a})


def vaccancydelete(request, id):
    a = vaccancyuploadmodel.objects.get(id=id)
    a.delete()
    return redirect(vaccancysuccess)


def userregistration(request):
    if request.method == 'POST':
        a = userregistrationform(request.POST)

        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        un = request.POST.get('username')
        em = request.POST.get('email')
        ps = request.POST.get('password')
        cp = request.POST.get('confirmpassword')  # getting directly from html form
        if ps == cp:
            b = User(username=un, first_name=fn, last_name=ln, email=em, password=ps)
            b.save()
            return redirect(userlogin)
        else:
            return HttpResponse("Incorrect password")
    # else:
    # return HttpResponse("Registration failed")

    else:
        return render(request, 'userregistration.html')


# def userlogin(request):
#     if request.method == 'POST':
#         a = userloginform(request.POST)
#         if a.is_valid():
#             em = a.cleaned_data['email']
#             ps = a.cleaned_data['password']
#             b = User.objects.all()
#             for i in b:
#                 if i.email == em and i.password == ps:
#                     return HttpResponse("Login success")
#             else:
#                 return HttpResponse("Login failed")
#     else:
#         return render(request, 'userlogin.html')


def userlogin(request):
    if request.method == 'POST':
        a = userloginform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            b = User.objects.all()
            for i in b:


                if i.email == em and i.password == ps:
                    # return redirect(userprofile)
                    return render(request,'userprofile.html')
            else:
                return HttpResponse("Login failed")
    else:
        return render(request, 'userlogin.html')


def userdetails(request):
    if request.method == 'POST':
        a = userdetailsform(request.POST, request.FILES)
        if a.is_valid():
            fn = a.cleaned_data['fullname']
            em = a.cleaned_data['email']
            rs = a.cleaned_data['resume']
            im = a.cleaned_data['image']
            eq = a.cleaned_data['educationalqualification']
            ex = a.cleaned_data['experience']
            ad = a.cleaned_data['address']
            mb = a.cleaned_data['mobile']
            b = userdetailsmodel(fullname=fn, email=em, resume=rs, image=im, educationalqualification=eq, experience=ex,
                                 address=ad, mobile=mb)
            b.save()
            # return HttpResponse("Details ulpoaded successfully !")
            return render(request, 'userprofile.html', {'un': fn})
            # return redirect(userprofile)
        else:
            return HttpResponse("Details uploading failed")
    return render(request, 'userdetails.html')


def userprofile(request):
    return render(request, 'userprofile.html')


def userviewvaccancy(request):
    a = vaccancyuploadmodel.objects.all()
    return render(request, 'userviewvaccancy.html', {'a': a})





def userdisplay(request):
    a = userdetailsmodel.objects.all()
    fullname = []
    email = []
    resume = []
    image = []
    education = []
    experience = []
    address = []
    mobile = []
    id = []
    for i in a:
        img = i.image
        image.append(str(img).split('/')[-1])
        fn = i.fullname
        fullname.append(fn)
        em = i.email
        email.append(em)
        res = i.resume
        resume.append(str(res).split('/')[-1])
        eq = i.educationalqualification
        education.append(eq)
        ex = i.experience
        experience.append(ex)
        ad = i.address
        address.append(ad)
        mob = i.mobile
        mobile.append(mob)
        id1 = i.id
        id.append(id1)
    mylist = zip(image,fullname,email,resume,education,experience,address,mobile,id)
    return render(request, 'userdisplay.html', {'mylist': mylist})




def userdetailsedit(request, id):
    a=filemodel.objects.get(id=id)
    img=str(a.image).split('/')[-1]#abc.png
    if request.method=='POST':
        a.filename=request.POST.get('filename')
        # IMAGE
        if len(request.FILES) !=0: #new file checking
            if len(a.file)!=0: #old file checking
                os.remove(a.file.path) #remove the old file using os
            a.file=request.FILES['file']
        a.save()
        return redirect(filedisp)


    return render(request,'editfile.html',{'a':a,'img':img})












def userdetailsdelete(request, id):
    a = userdetailsmodel.objects.get(id=id)
    if len(a.image)>0:
        os.remove(a.image.path)
    if len(a.resume)>0:
        os.remove(a.resume.path)
    a.delete()
    return redirect(userdisplay)


def editcompanyprofile(request,id):
    a = regmodel.objects.get(id=id)
    if request.method == 'POST':
        a.firstname = request.POST.get('firstname')
        a.lastname = request.POST.get('lastname')
        a.email = request.POST.get('email')
        a.phone = request.POST.get('phone')





        a.save()
        return redirect(display)
    return render(request, 'editcompanyprofile.html', {'a': a})



def jobapply(request,id):
    a = vaccancyuploadmodel.objects.get(id=id)
    cmp = a.companyname
    job = a.jobtitle
    id= a.id
    if request.method == 'POST':
        a = jobapplyform(request.POST,request.FILES)
        if a.is_valid():
            cn = a.cleaned_data['companyname']
            jt = a.cleaned_data['jobtitle']
            fn = a.cleaned_data['fullname']
            em = a.cleaned_data['email']
            rs = a.cleaned_data['resume']
            b = jobapplymodel(companyname=cn,jobtitle=jt,fullname=fn,email=em,resume=rs)
            b.save()
            subject = f"New job applied to {cmp}"
            message = f'Hi {fn} \n Your application for  {jt}  is applied successfully'
            email_from = EMAIL_HOST_USER  # from
            send_mail(subject, message, email_from,[em])
            return redirect(applysuccess)
        else:
            return HttpResponse("Failed")
    return render(request,'jobapply.html',{'cmp':cmp,'jt':job,'id':id})



def applysuccess(request):
    return render(request,'applysuccess.html')



def wishlist(request,id):
    a = vaccancyuploadmodel.objects.get(id=id)

    b = wishlistmodel(cid=id ,companyname = a.companyname,email = a.email,jobtitle = a.jobtitle,jobtype = a.jobtype,worktype = a.worktype,experiencerequired = a.experiencerequired,qualificationrequired = a.qualificationrequired)
    b.save()
    return redirect(mywish)



def mywish(request):
    a = wishlistmodel.objects.all()
    return render(request,'mywish.html',{'a':a})



def removewish(request,id):
    a = wishlistmodel.objects.get(id=id)
    a.delete()
    return redirect(mywish)



def viewappliedusers(request):
    a = jobapplymodel.objects.all()
    resume = []
    companyname = []
    jobtitle = []
    fullname = []
    email = []
    for i in a:
        res = i.resume
        resume.append(str(res).split('/')[-1])
        cn = i.companyname
        companyname.append(cn)
        jt = i.jobtitle
        jobtitle.append(jt)
        fn = i.fullname
        fullname.append(fn)
        em = i.email
        email.append(em)
    mylist = zip(fullname,email,companyname,jobtitle,resume)
    return render(request,'viewappliedusers.html', {'mylist': mylist})




def reg(request):
    if  request.method=='POST':
        a=regform1(request.POST)
        if a.is_valid():
            nm=a.cleaned_data['name']


            b=regmodel1(name=nm)
            b.save()
            return HttpResponse("success")
        else:
            return HttpResponse("failed")
    return render(request,'reg.html')

#login -->admin profile page -->(add  news feeds)-->newsfeed html page
#-->success




from django.contrib.auth import authenticate

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:

                  return HttpResponse("login success")
            else:
                return HttpResponse("login failed")

    return render(request, 'login.html',)



def jobapply(request,id):
    a = vaccancyuploadmodel.objects.get(id=id)
    cmp = a.companyname
    job = a.jobtitle
    id= a.id
    if request.method == 'POST':
        a = jobapplyform(request.POST,request.FILES)
        if a.is_valid():
            cn = a.cleaned_data['companyname']
            jt = a.cleaned_data['jobtitle']
            fn = a.cleaned_data['fullname']
            em = a.cleaned_data['email']
            rs = a.cleaned_data['resume']
            ac_no="15"+ph
            b = jobapplymodel(companyname=cn,jobtitle=jt,fullname=fn,email=em,resume=rs)
            b.save()
            subject = "your account has been created"
            message = f"your new account number is {ac_no}"
            email_from = "abc@gmail.com"
            email_to=em
            send_mail(subject, message, email_from,[email_to])
            return redirect(applysuccess)
        else:
            return HttpResponse("Failed")
    return render(request,'jobapply.html',{'cmp':cmp,'jt':job,'id':id})


def display(request):
    a=regmodel.objects.all() #[(1,arjun,gw),(2,akhil,)]
    return render(request,'display.html',{'data':a})

#














