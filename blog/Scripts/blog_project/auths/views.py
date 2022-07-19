from django.shortcuts import render , redirect
from .models import User
from django.contrib.auth import authenticate ,login , logout

def registeruser(req):
	if req.method == "POST":
		name = req.POST['name']
		email = req.POST['email']
		password = req.POST['password']
		confirm_password = req.POST['confirmpassword']
		if password == confirm_password:
			user = User.objects.create_user(email=email,fullname=name,password=password)
			user.save()
			users = User.authenticate(req, email=email, password=password)
			if users is not None:
				login(req, users)
				return redirect('/')

	return render( req ,'register.html' )



def loginuser(req):
	if req.method == "POST":
		email = req.POST['email']
		password = req.POST['password']
		users = authenticate(req, email=email, password=password)
		if users is not None:
			login(req, users)
			return redirect('/')
	return render(req , 'login.html')


def userlogout(req):
	logout(req)
	return redirect('/')
