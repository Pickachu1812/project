from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import main


def projarka(request):
  response = main()
  return JsonResponse(response, safe=False)
  
def home(request):
  return render(request, 'home.html')
 
def projarka_view(request):
  row = main()
  return render (request, 'projarka_view.html', row) 
  

