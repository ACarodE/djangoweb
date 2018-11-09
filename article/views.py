from django.shortcuts import render,HttpResponse
from django.views.generic import View
from .models import Article



# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def ishukuku(request):
    return render(request,"ishukuku.html")
def teampage(request):
    return render(request,"teampage.html")
def workpage(request):
    return render(request,"workpage.html")


def articles(request):
    template_name= 'articles.html'
    queryset=Article.objects.all()
    
    context={
        "object_list":queryset
    }
    return render(request,template_name,context)






    



    