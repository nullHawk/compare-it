from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
def front_end(request):
    return render(request, 'compare/index.html')
def compare(request):
    data ={"name":"just testing"}
    return JsonResponse(data)
