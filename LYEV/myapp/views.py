from django.shortcuts import render
# importing loading from django template
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

def index(request):
    template = loader.get_template('index.html') # our template
    return HttpResponse(template.render())  # rendering template in HttpResponse
    
@csrf_exempt
def signIn(request):
    if request.method == 'POST':
        email = request.POST["emailId"]
        password = request.POST["password"]
        # add sql code to check if correct sql login is done or not
        request.session['user_email'] = email # creating a session
        return redirect("/")  # redirect to index page after successful sign in
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
        # add sql code to store signUp details
        request.session['user_email'] = email # creating a session
        return redirect("/")  # redirect to index page after successful sign up
    else:
        template = loader.get_template('signUp.html') # our template
        return HttpResponse(template.render())  # rendering template in HttpResponse

def logOut(request):
    if 'user_email' in request.session:
        for key, value in request.session.items():
            print('{} => {}'.format(key, value))
        del request.session['user_email']
        return redirect("/") # redirect to index page after successful log out
    else:
        for key, value in request.session.items():
            print('{} => {}'.format(key, value))
        return HttpResponse("Error")