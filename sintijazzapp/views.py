from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    data = {"name": "Dean", "age": 55}
    context = {"data": data}
    
    return render(request,"sintijazzapp/index.html",context)