from django.shortcuts import render
from myapp.models import Contact, Profile
from django.http import HttpResponse,JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact_us(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get("name")
        em = request.POST.get("email")
        sub = request.POST.get("subject")
        mas = request.POST.get("message")

        obj = Contact(name=name, email=em, subject=sub, message=mas, )
        obj.save()
        context['message'] = f"Dear {name}, Thanks for your time" 
           
    return render(request,'contact.html', context)




def register(request):
    context={}
    if request.method=="POST":
        #fetch data from html form
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        contact = request.POST.get('number')
        check = User.objects.filter(username=email)
        if len(check)==0:
            #Save data to both tables
            usr = User.objects.create_user(email, email, password)
            usr.first_name = name
            usr.save()

            profile = Profile(user=usr, contact_number = contact)
            profile.save()
            context['status'] = f"User {name} Registered Successfully!"
        else:
            context['error'] = f"A User with this email already exists"

    return render(request,'register.html', context)

def check_user_exists(request):
    email = request.GET.get('usern')
    check = User.objects.filter(username=email)
    if len(check)==0:
        return JsonResponse({'status':0,'message':'Not Exist'})
    else:
        return JsonResponse({'status':1,'message':'A user with this email already exists!'})
















def feature(request):
    return render(request,'feature.html')


def blog(request):
    return render(request,'blog.html')


def booking(request):
    return render(request,'booking.html')

def about(request):
    return render(request,'about.html')

def team(request):
    return render(request,'team.html')

def base(request):
    return render(request,'base.html')


