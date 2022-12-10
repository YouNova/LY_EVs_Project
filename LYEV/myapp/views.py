from django.shortcuts import render
# importing loading from django template
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    template = loader.get_template('index.html') # our template
    return HttpResponse(template.render())  # rendering template in HttpResponse
    
def signIn(request):
    if request.method == 'POST':
        email = request.POST["emailId"]
        password = request.POST["password"]
        # do something
    else:
        template = loader.get_template('signIn.html') # our template
        return HttpResponse(template.render())  # rendering template in HttpResponse
    
@csrf_exempt
def signUp(request):
    if request.method == 'POST':
        email = request.POST["emailId"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        trckingConf = request.POST["confVal"]
        # do something
    else:
        template = loader.get_template('signUp.html') # our template
        return HttpResponse(template.render())  # rendering template in HttpResponse