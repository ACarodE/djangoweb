from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import View
from django.contrib import messages






from .forms import ContactMessage # Add this


def contactpage(request):
    form=ContactMessage()
    context = {
        "form" : form
    }
    return render(request,"contactpage.html", context)
def contactpage(request):
    if request.method == 'POST':
        form = ContactMessage(request.POST)
        if form.is_valid():
            contact= form.save(commit= False)
            contact.save()
            
            # send email code goes here
            
            return HttpResponse('Bize ulaştığınız için teşekkür ederiz!')
    else:
        form = ContactMessage()

    return render(request, 'contactpage.html', {'form': form})












