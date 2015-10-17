import logging
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from portal.forms import QuestionForm
from portal.models import Question


def index(request):
	if request.user.is_authenticated():
		return redirect("/portal/dashboard/")	
	else :
		return render(request, 'portal/index.html')

def signin(request):
	if request.user.is_authenticated():
		return redirect("/portal/dashboard/")	
	else :
		return render(request, 'portal/login.html')	

def signup(request):
	if request.user.is_authenticated():
		return redirect("/portal/dashboard/")	
	else :
		return render(request, 'portal/signup.html')		

@login_required(login_url='/portal/')
def dashboard(request):
	return render(request, 'portal/dashboard.html', {"session":request.session})

@login_required(login_url='/portal/')
def postquestion(request):
	try:
		data = QuestionForm(request.POST)
		print data
		if data.is_valid() == True :
			data.save()
			return HttpResponse("Question posted Successfully")	
		return HttpResponse("Question could not be posted")	
	except Exception, e:
		logging.exception('')

def registeruser(request):
	Username = request.POST['Username']	
	email = request.POST['email']	
	password = request.POST['password']	
	last_name = request.POST['category']	
	user = User.objects.create_user(Username, email, password)
	user.last_name =  last_name
	user.save()
	return HttpResponse("User Registerd Successfully")


@login_required(login_url='/portal/')
def verifyAnswer(request):
	answer = request.POST['answer']
	question = request.POST['question']
	keywords = str(Question.objects.filter(question=question).first().keywords).split(',')
	answerList = answer.split()
	percentage = len(set(keywords) & set(answerList))*100.0/len(keywords)
	return HttpResponse(percentage)		

@login_required(redirect_field_name='/portal/')
def user_logout(request):
	logout(request)
	return redirect("/portal/")

def verify(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
	    if user.is_active:
	    	login(request, user)
	    	request.session['category'] = user.last_name
	    	return redirect("/portal/dashboard/")	
	    else:
	        print("The password is valid, but the account has been disabled!")
	else:
	    print("The username and password were incorrect.")	
	    return redirect("/portal/")	