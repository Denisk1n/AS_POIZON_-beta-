from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   return HttpResponse("<h1> Проверка работы </h1>")


def about(request):
   return HttpResponse("<h2> Не много информации о нас :)</h2>")