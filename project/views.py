from django.http import HttpResponse,HttpResponseRedirect

from django .shortcuts import render
from .forms import usersForm
from service.models import Service
from contactenquiry.models import contactEnquiry
from news.models import News
from django.core.paginator import Paginator
def home(request):
    newsData = News.objects.all()
    servicesData=Service.objects.all().order_by('service_title')

    data={
        'servicesData':servicesData,
        'newsData':newsData

    }
    return render(request,"index.html",data)

def newsDetails(request,slug):
    newsDetails=News.objects.get(news_slug=slug)
    data = {
        'newsDetails':newsDetails
    }
    return render(request,"newsdetails.html",data)

def about(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request,"about.html",{'output':output})

def service(request):
    servicesData=Service.objects.all().order_by('service_title')
    # if request.method=="GET":
    #     st=request.GET.get('servicename')
    #     if st!=None:
            # servicesData = Service.objects.filter(service_title__icontains=st)
    paginator = Paginator(servicesData,2)
    page_number=request.GET.get('page')
    servicesDataFinal = paginator.get_page(page_number)
    totalpage=servicesDataFinal.paginator.num_pages
    data={
        'servicesData':servicesDataFinal,
        'lastpage':totalpage,
        'totalPagelist':[n+1 for n in range(totalpage)]
    }
    return render(request,"service.html",data)

def contact(request):
    return render(request,"contact.html")

def saveEnquiry(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        en=contactEnquiry(name=name,email=email,subject=subject,message=message)    
        en.save()
        return render(request,"contact.html")

def blog(request):
    return render(request,"blog.html")

def detail(request):
    return render(request,"detail.html")

def price(request):
    return render(request,"price.html")

def test(request):
    return render(request,"team.html")

def testimonial(request):
    return render(request,"testimonial.html")

# def userForm(request):
#     finalans=0
#     fn=usersForm()
#     data = {'form':fn}
#     try:
#         if request.method=="POST":

#             n1=int(request.POST.get('num1'))
#             n2=int(request.POST.get('num2'))
#             n3=int(request.POST.get('num3'))
#             finalans=n1+n2+n3
#             data={
#                 'form':fn,
#                 'output':finalans
#              }
#             # url="/about/?output={}".format(finalans)
#             return HttpResponse(finalans)
#     except:
#             pass
        

def submitform(request):
    try:
        if request.method=="POST":

            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            n3=int(request.POST.get('num3'))
            finalans=n1+n2+n3
            data={
                'n1':n1,
                'n2':n2,
                'n3':n3,
                'output':finalans
             }
            # url="/about/?output={}".format(finalans)
            return HttpResponse(finalans)
    except:
            pass

def calculator(request):
    return render(request,"calculator.html")

def userForm(request):
    finalans=0
    fn=usersForm()
    data={'form':fn}
    try:
        if request.method=="POST":

            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            n3=int(request.POST.get('num3'))
            finalans=n1+n2+n3
            data={
                'form':fn,
                'output':finalans
             }
            url="/about/?output={}".format(finalans)
            return HttpResponseRedirect(url)
    except:
     pass
    return render(request,"userform.html",data)

def calculator(request):
    c=''
    try:
        if request.method == "POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=="+":
                c=n1+n2;
            elif opr=="-":
                c=n1-n2;
            elif opr=="*":
                c=n1*n2;
            elif opr=="/":
                c=n1/n2;    


    except:
        c-"Invalid opr..."

    return render(request,"calculator.html",{'c':c})

def evenodd(request):
    c=''
    try:
        if request.method == "POST":
            n=int(request.POST.get('num1'))
            if n%2==0:
                c="Even Number"
            else:
                c="Odd Number"

    except:
        c-"Invalid opr..."

    return render(request,"evenodd.html",{'c':c})

def marksheet(request):
        if request.method == "POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            n3=eval(request.POST.get('num3'))
            n4=eval(request.POST.get('num4'))
            n5=eval(request.POST.get('num5'))
            t=n1+n2+n3+n4+n5
            p=t*100/500;
            if p>=60:
                d="First Division"
            elif p>=48:
                d="Second Division"
            elif p>=35:
                d="Third Division"
            else:
                d="Fail"
            data={
                'total':t,
                'percentage':p,
                'div':d
            }
            return render(request,"marksheet.html",data)  

        return render(request,"marksheet.html") 
        