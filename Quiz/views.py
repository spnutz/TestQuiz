from django.http import HttpResponse
from django.shortcuts import redirect, render
from Quiz.models import Question

def home_page(request):
    if request.method == 'POST':
        Question.objects.create(question=request.POST.get('quizbox'))
        Question.objects.create(ans=request.POST.get('answer'))
        quiz_item = Question.objects.all()
        return render(request, 'home.html', {'quiz_item':quiz_item})
    
    return render(request, 'home.html')
