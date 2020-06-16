from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	return HttpResponse('<html><title>To-Do lists</title></html>')

def about(request):
	return HttpResponse('<h1>This is about page</h1>')

def account(request):
	return HttpResponse('<h1>This is account page</h1>')