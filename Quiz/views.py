from django.http import HttpResponse
from django.shortcuts import redirect, render
from Quiz.models import Question, Choice
from django.shortcuts import get_list_or_404, get_object_or_404

def home_page(request):
    return render(request, 'home.html')

def createquiz(request):
    if request.method == 'POST':
        q = Question(question_text=request.POST.get('quizbox',''),ans=request.POST.get('answer',''))
        q.save()
        
        c = Choice(choice1=request.POST.get('a',''),
            choice2=request.POST.get('b',''),
             vote_T=0, vote_F=0, question=q)
        c.save()
        

        return redirect('http://localhost:8000/quiz/')

    quiz_item = Question.objects.all()

    return render(request, 'createquiz.html', {'quiz_item':quiz_item})
    
   

def goQuiz(request):
    show_quiz = Question.objects.all()
    return render(request, 'answer.html', {'show_quiz':show_quiz})

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        choice_item = Choice.objects.get(question=question_id)
    except Question.DoesNotExits:
        raise Http404("Question does not exits")
    return render(request, 'detail.html', {'question':question, 'choice_item':choice_item})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        answer = request.POST.get('choice')
        check_ans = Question.objects.get(id=question_id).ans
        vote = Choice.objects.get(question=question_id)

        if answer == check_ans:
            vote.vote_T += 1
            vote.save()
            return render(request, 'resultT.html', {'vote':vote})
        else:
            vote.vote_F += 1
            vote.save()
            return render(request, 'resultF.html', {'vote':vote})
    return HttpResponse("You're voting on question %s." % question_id)
