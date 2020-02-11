from django.shortcuts import render

def index(request):
	return render(request,"guestapp/index.html")
def about(request):
	return render(request,"guestapp/about.html")
def contact(request):
	return render(request,"guestapp/contact.html")