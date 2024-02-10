from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        "title":"home",
        "h1":"Заголовок H1",
        "content":"Главная страница магазина",
        'list':['first','second'],
        'dict':{'first':1},
        'is_autenticated':True
    }
    return render(request,'home/index.html',context)

def about(request):
    return HttpResponse('About')

