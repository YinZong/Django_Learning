from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, Django. Nice 2 meet u.")

def year_archiv(request, year):
    return HttpResponse("Year: " + str(year))

def montu_archiv(request, year, month):
    return HttpResponse("Year: " + str(year) + " , Month: " + str(month))