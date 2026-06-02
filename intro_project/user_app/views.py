from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def greet(request):
    return HttpResponse("Hi this is greeting")

def getname(request):
    return HttpResponse("hello vinit here")


# NEW API
def users(request):

    data = [
        {
            "name": "Pavan",
            "email": "pavan@email.com",
            "address": "Hyderabad"
        },
        {
            "name": "Sai",
            "email": "sai@email.com",
            "address": "Guntur"
        },
        {
            "name": "Dhanush",
            "email": "dhanush@gmail.com",
            "address": "Rajamundry"
        }
    ]

    return JsonResponse(data, safe=False)

def greet_to_user(request,name):
    return HttpResponse(f"Hi {name},Greeting")


# Correct URLs
# http://127.0.0.1:8000/user/message/
# http://127.0.0.1:8000/user/getname/
# http://127.0.0.1:8000/user/users/
# http://127.0.0.1:8000/user/greet/vinit/