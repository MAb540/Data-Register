from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib import messages

def Home(request):
	return render(request,'users/home.html')





def Register(request):

	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			s_n = form.cleaned_data['Full_Name']
			messages.success(request,f'Your Data has been saved.')
			return redirect('home')
	else:
		form = UserRegisterForm()
		context = {'form':form}		
	return render(request,'users/register.html',context)

