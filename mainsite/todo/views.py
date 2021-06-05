from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
# Create your views here.

def index(request):
	#tasks is from models.py
	tasks = Task.objects.all()

	#form is object of TaskForm from forms.py 
	form = TaskForm() 

	#check if the form action="/" has valid data or not to post it in the server 
	if request.method=='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')


	#pass the context to templates as dictionary to render
	context = {'tasks': tasks,'form':form}

	return render(request,'todo/list.html',context)

def create(request):
	tasks = Task.objects.all()

	form = TaskForm()
	
	if request.method=='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {'tasks': tasks,'form':form}
	return render(request,'todo/create.html',context)

def update(request,pk):
	task = Task.objects.get(id=pk)
	form = TaskForm(instance=task) #instance makes the use of the same form

	#check if the form action="/" has valid data or not to post it in the server 
	if request.method=='POST':
		form = TaskForm(request.POST,instance=task)
		if form.is_valid():
			form.save()
		return redirect('/')

	#pass the context to templates as dictionary to the render
	context={'form':form}

	return render(request,'todo/update.html',context)


def delete(request,pk):

	task = Task.objects.get(id=pk)

	if request.method=='POST':
		task.delete()
		return redirect('/')
		
	context={'task':task}

	return render(request,'todo/delete.html',context)