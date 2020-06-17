from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	if request.method == 'POST':
		return HttpResponse(reqeust.POST['item_text'])
	return render(request, 'home.html', {})

def about(request):
	return HttpResponse('<h1>This is about page</h1>')

def account(request):
	return HttpResponse('<h1>This is account page</h1>')