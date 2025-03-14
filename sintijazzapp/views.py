from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    data = ["Oatmeal", "Grits", "Yogurt", "Cottage Cheese"]
    context = {"foods": data}
    return render(request,"sintijazzapp/index.html",context)



