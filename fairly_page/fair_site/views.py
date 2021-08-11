from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
def register_request(request):
    if request.method=='POST':       #check if the form is being posted
        form=NewUserForm(request.POST)
        if form.is_valid():             #check if the form is valid
            user=form.save()
            login(request,user)
            messages.success(request,"Registration successful.")
            return redirect("fair_site:fair_site")
        messages.error(request,"Unsuccessful registration.Invalid information")
    form=NewUserForm()
    return render(request=request,template_name='fair_site/register_fair.html',content={'form':form})
