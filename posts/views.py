from django.shortcuts import render
from django.http import HttpResponse

def http_response(request):
    return HttpResponse('Hello World from Http!')

def html_response(request):
    return render(request, 'index.html')