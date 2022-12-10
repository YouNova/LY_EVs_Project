from django.shortcuts import render
# importing loading from django template
from django.template import loader
# Create your views here.
from django.http import HttpResponse

def index(request):
    template = loader.get_template('index.html') # our template
    return HttpResponse(template.render())  # rendering template in HttpResponse
    
def signIn(request):
    template = loader.get_template('signIn.html') # our template
    return HttpResponse(template.render())  # rendering template in HttpResponse
    
def signUp(request):
    template = loader.get_template('signUp.html') # our template
    return HttpResponse(template.render())  # rendering template in HttpResponse