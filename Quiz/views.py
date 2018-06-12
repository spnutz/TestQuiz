from django.http import HttpResponse
from django.shortcuts import redirect, render
from Quiz.models import Question

def home_page(request):
    return render(request, 'home.html')

def createquiz(request):
    if request.method == 'POST':
        Question.objects.create(question=request.POST.get('quizbox',''), ans=request.POST.get('answer',''))
        quiz_item = Question.objects.all()
        return render(request, 'createquiz.html', {'quiz_item':quiz_item})
    
    return render(request, 'createquiz.html')

def goQuiz(request):
    show_quiz = Question.objects.all()
    return render(request, 'answer.html', {'show_quiz':show_quiz})
