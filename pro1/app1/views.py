from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.
def index(re):
    return render(re,'index.html')
def cont(re):
    dd=Client.objects.all()
    return render(re,'admin_view_contact.html',{'data':dd})
def cl_c_admn(re):
    return render(re,'client_contact_admin.html')
# def admn_v_proj(re):
#     return render(re,'client_view_projects.html')
def con(re):
    return render(re,'contact.html')
def proj(re):
    return render(re,'projects.html')
def services(re):
    return render(re,'services.html')
def about(re):
    return render(re,'about.html')
# Create your views here.
def adminViewPro(re):
    dd=Project.objects.all()
    return render(re,'admin_view_projects.html',{'data':dd})
def register(re):
    if re.method=='POST':
        a=re.POST['n1']
        b=re.POST['n2']
        c=re.POST['n3']
        d=re.POST['n4']
        e=int(re.POST['n5'])
        f=re.POST['n6']
        data=Client.objects.create(client_name=a,client_email=b,c_username=c,c_password=d,client_phone=e,client_msg=f)
        data.save()
        print("hi")
        return HttpResponse("Contact Registered")
        # messages.success(re,"Contact succesfully registered:)")
        # return render(re,'contact.html')
    return render(re,'contact.html')
def blog(re):
    d = Project.objects.all()
    return render(re,'blog.html',{'data':d})
def login_pg(re):
    return render(re,'login.html')
def profile(re):
    return render(re,'adminProfile.html')
def logi(re):
    if re.method == 'POST':
        u = re.POST['n1']
        p = re.POST['n2']

        if u =='admin' and p == 'admin' :
            re.session['id'] = u
            return render(re,'adminProfile.html')
        else:
            messages.info(re, "invalid Password")
            return render(re,'login.html')

    else:
        return render(re, 't_login.html')


    # if re.method=='POST':
    #     u=re.POST['n1']
    #     p=re.POST['n2']
    #     d=Admin.objects.get(loginname=u)
    #     if d.password==p:
    #         # re.session['id']=u
    #         # return redirect(profile)
    #         return render(re,'adminProfile.html')
    #     else:
    #         return HttpResponse("invalid password")
    #
    # else:
    #     return render(re,'login.html')

def add_project(re):

    return render(re,'admn_add_projects.html')
def addPro(re):
    if re.method=='POST':
        a=re.POST['n1']
        b=re.POST['n2']
        c=re.FILES['n3']
        d=re.POST['n4']
        e=re.POST['n5']
        f=re.POST['n6']
        data=Project.objects.create(proj_name=a,proj_budjet=b,proj_img=c,proj_dur=d,proj_date=e,proj_details=f)
        data.save()
        messages.success(re,"NEw project succesfully added...!")
        return render(re,'admn_add_projects.html')
        # return HttpResponse("NEw project succesfully added...!")


def adhd(re):
    d=Project.objects.all()
    return render(re,'adminHead.html',{'data':d})
def client_v_pro(re):
    d = Project.objects.all()
    return render(re,'blog.html',{'data':d})

def ppup(re):
    return render(re,'admin_update_project.html')
    # if re.method == 'POST':
    #     a = re.POST['n1']
    #     b = re.POST['n2']
    #     c = re.POST['n3']
    #     d = re.FILES['n4']
    #     e = re.POST['n5']
    #     f = re.POST['n6']
    #     Project.objects.filter(proj_name=a).update(proj_budjet=b, proj_dur=c, proj_img=d, proj_date=e, proj_details=f)
    #     return HttpResponse('updated')
    # s=Project.objects.all()

#     return render(re,'admin_update_project.html')
# def new_up(re):
#     if re.method=='POST':
#         a=re.POST['n1']
#         b=re.POST['n2']
#         c=re.FILES['n3']
#         d=re.POST['n4']
#         e=re.POST['n5']
#         f=re.POST['n6']
#         Project.objects.filter(proj_name=a).update(proj_budjet=b,proj_img=c,proj_dur=d,proj_date=e,proj_details=f)
#         return render(re,'adminProfile.html')
#
#     return HttpResponse('not going to if ')
def Pdelete(re,a):
    data=Project.objects.filter(proj_name=a)
    data.delete()
    messages.success(re,"The Project have been deleted..!")
    return redirect(adminViewPro)