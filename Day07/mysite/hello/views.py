from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
def demo(request):
#def home(request):
    temp=loader.get_template('tables.html')
    return HttpResponse(temp.render())
    #return HttpResponse("Hello, Django!")
