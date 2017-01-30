from django.shortcuts import render
def home(request):
	context = {}
	response = "home.html"
	return render(request, response, context)