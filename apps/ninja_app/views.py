from django.shortcuts import render, HttpResponse, redirect

def index(request):
	response = " work "
	return HttpResponse(response)