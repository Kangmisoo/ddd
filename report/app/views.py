from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request) :
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
   # return HttpResponse("<h1> 안녕하세요 홍길동입니다. </h1> ")
