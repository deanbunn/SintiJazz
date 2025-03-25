#from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    data = ["Oatmeal", "Grits", "Yogurt", "Cottage Cheese", "Eggs"]
    context = {"foods": data, "record_size": 45}
    return render(request,"sintijazzapp/index.html",context)



