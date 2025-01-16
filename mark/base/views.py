from django.shortcuts import render
from other.models import *

# Create your views here.
def home(request):
    staffs = Staff.objects.filter(show_on_home=True)
    project = Project.objects.filter(show_on_home=True)
    service = Service.objects.all().order_by('heading')
    review = Review.objects.all()[:4]
    foot_service = service[:4]
    blog = Blog.objects.all()[:6]
    foot_blog = Blog.objects.all()[:4]
    single_blog = Blog.objects.all()
    contact = ''
    try:
        contact = Contact.objects.all()[0]
    except:
        pass
    context = {
        'foot_blog':foot_blog,
        'blog':blog,
        'foot_service':foot_service,
        'review':review,
        "staffs" : staffs,
        'project': project,
        'service' : service,
        'contact' :contact,
        'single_blog':single_blog
    }
    return render(request,'index.html',context)


