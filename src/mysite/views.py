from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	# if request.method == 'POST':
	# 	return HttpResponse(request.POST['item_text'])
	return render(request, 'home.html', {
		'new_item_text': request.POST.get('item_text'),
	})

def about(request):
	return HttpResponse('<h1>This is about page</h1>')

def account(request):
	return HttpResponse('<h1>This is account page</h1>')