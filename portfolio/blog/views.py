from django.shortcuts import render,get_object_or_404,redirect
from . import views
from .models import Portfolio,Blog
from .forms import BlogForm,PortForm
from django.contrib import messages
# Create your views here.
def index(request):
    blogs=Portfolio.objects.all()
    context={
        'blogs':blogs
    }

    return render(request,'portfolio/index.html',context)

def portfolio(request,blog_id):
    blogs=get_object_or_404(Portfolio,id=blog_id)
    context={
        'blogs':blogs
    }
    return render(request,'portfolio/portfolio.html',context)

def detail(request,blog_id):
    blogs = get_object_or_404(Portfolio, id=blog_id)
    context = {
        'blogs': blogs
    }
    return render(request, 'portfolio/detail.html', context)


def contact(request):
    if request.method == "POST":
        form = BlogForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('list')

        else:
            messages.info(request, "please fill all data ")
            return render(request, 'portfolio/contact.html')
    else:
        form=BlogForm()
        return render(request, 'portfolio/contact.html', {'forms':form})

def list(request):
    blog=Blog.objects.all()
    context={
        'blogs':blog
    }
    return render(request,'portfolio/list.html',context)


def create(request):
    form=PortForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.info(request,"please fill all the data ")
            return render(request, 'portfolio/create.html')
    else:
        form = PortForm()
        return render(request, 'portfolio/create.html', {'forms': form})




def about(request):
    blogs = Portfolio.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request,'portfolio/about.html',context)





