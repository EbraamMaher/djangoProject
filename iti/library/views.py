from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def gethomepage(request):
    return HttpResponse("my home page")


def hompageHtml(request):
    return render(request,'library/homepage.html')
