from django.http import HttpResponse
from django.shortcuts import redirect, render
from Quiz.models import Question

def home_page(request):
    
    return render(request, 'home.html')
