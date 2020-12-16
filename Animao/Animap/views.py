from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def login(request):
	return render(
        request,
        'registration/login.html')
	
def index2(request):
	return render(
        request,
        'index2.html')
	
def Instruction(request):
	return render(
		request, 
		'Instruction.html')
def Menu(request):
	return render(
		request, 
		'Menu.html')
 