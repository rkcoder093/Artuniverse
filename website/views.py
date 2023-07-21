from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"website/index.html")

def about(request):
    return render(request,"website/about.html")


def mentor(request):
    return render(request,"website/mentor.html")

def result(request):
    return render(request,"website/result.html")

def internship(request):
    return render(request,"website/internship.html")