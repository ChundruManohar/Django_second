from django.shortcuts import render
from .models import Contact,About
# Create your views here.
def home(request):
    return render(request,'testapp/home.html')

def about(request):
    data = About.objects.all()
    context =  {
        'data':data
    }
    return render(request,'testapp/about.html',context)

def contact(request):
    if request.method=="POST":
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        city = request.POST['city']
        state = request.POST['state']
       
        c = Contact(first_name=f_name,Last_name=l_name,email=email,city=city,state=state,)
        c.save()
        return render(request,'testapp/contact.html')
        
    return render(request,'testapp/contact.html')