from django.shortcuts import render,redirect
from django.http import HttpResponse
from .utils import  fill_nan
import pandas as pd
from .graph import Graph
# Create your views here.

df = None

def index(request):
    global df
    chart = None
    ls = None
    if request.method == "POST":
        if request.POST.get("fileBu"):
            file = request.FILES['document']
            df = pd.read_csv(file)
            fill_nan(df)
            cols = list(df.columns)
            return render(request, 'index.html', {'data': cols})
        elif request.POST.get("colBu"):
            data = request.POST.getlist("columns")
            chart = Graph(df, *data).get_suitable_plots()
    return render(request, 'index.html', {'chart': chart})


# def printHello(request):
# 	return HttpResponse("Hello")
#
# def index(request):
#     context = {
#         "data" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     }
#     return render(request,'index.html',context)
#
# def ColumnsSelection(request):
#     if request.method=="POST":
#         data = request.POST.getlist('columns')
#         return render(request,'index.html',{'dataset':data})
#         print(data)
#     return render(request,'index.html')
#
# def upload(request):
#     if request.method == 'POST':
#         uploaded_file = request.FILES['document']
#         print(uploaded_file.name)
#         print(uploaded_file.size)
#     return render(request,'index.html')