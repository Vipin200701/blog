
from django.http import HttpResponse
from django.shortcuts import render
from blogs.admin import education
from blogs.models import new, Category
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    detail = Category.objects.all().order_by('Title')[:3]
    if request.method=="GET":
        st=request.GET.get('catagoryname')
        if st!=None:
            detail = Category.objects.filter(Title__icontains=st)

    data1={
        'detail':detail
    }
    return render(request,'index.html',data1)


def about(request):
    newdata=new.objects.all()
    data={
        'newdata':newdata
    }
    return render(request, 'about.html',data)
    
def form(request):
    return render(request,'form.html')

def travel(request):
    detail = Category.objects.all().order_by('Title')

    #page in template
    paginator=Paginator(detail,4)
    page_number=request.GET.get('page')
    ServiceDatafinal=paginator.get_page(page_number)


    #  Search bar
    if request.method=="GET":
        st=request.GET.get('catagoryname')
        if st!=None:
            detail = Category.objects.filter(Title__icontains=st)
    data1={
        'detail':detail,
        'detail':ServiceDatafinal,
    }
    return render(request, 'Category.html',data1)

def register(request):
    return render(request,'form.html')

def cate(request):
    detail = Category.objects.all()
    
    data1={
        'detail':detail,
    }
    return render(request, 'Traveling.html',data1)

def food(request):
    detail = Category.objects.all()
    data1={
        'detail':detail,
    }
    return render(request, 'food.html',data1)

    