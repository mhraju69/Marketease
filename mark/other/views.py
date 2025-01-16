from django.shortcuts import render
from django.shortcuts import render
from other.models import *
from django.http import HttpResponse
import requests
from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.

def service(request):
    service = Service.objects.all().order_by('heading')
    single = "No Services Avaliable"
    if service:
        single = service.first()
    slug = ''
    if request.method == 'POST':
        slug = request.POST['service_choice']
        single = Service.objects.filter(slug = slug).first()
    context= {
        'selected_slug' : slug, 
        'service' :service,
        'single' : single
    }
    return render(request,'service.html',context)




def single_service(request,slug):

    single = Service.objects.filter(slug = slug).first()
    service = Service.objects.all().order_by('heading')
    if request.method == 'POST':
        slug = request.POST['service_choice']
        single = Service.objects.filter(slug = slug).first()
    context= {
        'selected_slug' : slug, 
        'service' :service,
        'single' : single
    }
   
    return render(request,'service.html',context)






   
def projects(request):
    return render(request,'current.html')

def blog(request):
    blog = Blog.objects.all().order_by('create')
    if 'search' in request.GET :
        search = request.GET['search']
        blog = Blog.objects.filter(title__contains=search)
    paginator = Paginator(blog , 12)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    service = Service.objects.all().order_by('heading')
    foot_service = service[:4]
    foot_blog = Blog.objects.all()[:4]
    contact = ''
    try:
        contact = Contact.objects.all()[0]
    except:
        pass
    context = {
        'foot_blog':foot_blog,
        'foot_service':foot_service,
        'page' : page,
        'service' : service,
        'contact' :contact
    }
    
    return render(request,'blog.html',context)


def blog_detail(request,slug):
    blog = Blog.objects.get(slug=slug)
    response = requests.get(blog.blog_link)
    return HttpResponse(response.content)



def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        new = Message(name = name, email = email , message = message)
        new.save()
        # print(name,email,message)
        
        messages.success(request,'Message sent succesfull. We will contact you within 24 Hour.')
        return redirect('contact')
    service = Service.objects.all().order_by('heading')
    contact = ''

    try:
        contact = Contact.objects.all()[0]
    except:
        pass
    
    context = {
        'contact':contact,
        'service' : service
    }
    return render(request,'contact.html',context)




def about(request):
    service = Service.objects.all().order_by('heading')
    foot_service = service[:4]
    foot_blog = Blog.objects.all()[:4]

    staff =Staff.objects.all()
    review = Review.objects.all()[:4]
    contact = ''
    try:
        contact = Contact.objects.all()[0]
    except:
        pass
    

    context = {
        'contact' :contact,
        'review':review,
        'staff':staff,
        'service' : service,
        'foot_service' : foot_service,
        'foot_blog' : foot_blog 
    }
    return render(request,'about.html',context)
