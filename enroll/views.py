
from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def sign_up(request):
 if request.method=="POST":
  fm = SignUpForm(request.POST)
  if fm.is_valid():

   fm.save()
 else:
  fm=SignUpForm()
 return render(request,'enroll/signup.html',{'form':fm})


def user_login(request):
  if request.method=='POST':
    fm =AuthenticationForm(request=request,data=request.POST)
    if fm.is_valid():
      uname=fm.cleaned_data['username']
      upass=fm.cleaned_data['password']
      user=authenticate(username=uname,password=upass)
      if user is not None:
        login(request,user)
        return HttpResponseRedirect('/profile/')
  else:
   fm = AuthenticationForm()
  return render(request,'enroll/loginuser.html',{'form':fm})


