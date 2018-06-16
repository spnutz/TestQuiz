from django.template.loader import render_to_string
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from Quiz.views import home_page
from Quiz.models import Question, Choice

class HomePageTest(TestCase):
    def teat_root_url_reolve_to_home_page_view(self):
        found = resolve('/quiz/')
        self.assertEqual(found.func, home)


class CreateChoicePageTest(TestCase):
    def test_create_choice_page(self):
        response = self.client.get('/quiz/createquiz/')
        self.assertTemplateUsed(response, 'createquiz.html')


    def test_show_quiz_page(self):
        response = self.client.get('/quiz/goQuiz/')
        self.assertTemplateUsed(response, 'answer.html')

   




#class AnsPageTest(TestCase):
#    def test_use_answer_page(self):
#        found = resolve('answer/')
 #       self.assertEqual(found.func, goQuiz)

class QuestionModel(TestCase):
    def test_can_save_model(self):
        frist_question = Question()
        frist_question.question_text = ' Dog is animal ?'
        frist_question.save()

        first_ans = Question()
        first_ans.ans = 'True'
        #first_ans.save()


        save_question = Question.objects.all()
        #print(save_question)
        self.assertEqual(save_question.count(), 1)

        #save_ans = Question.objects.all()
        #self.assertEqual(save_ans.count(), 1)
class ChoiceModel(TestCase):
    def test_can_save_model_choice(self):
        choice_1 = Choice()
        choice_1.choice1 = 'True'
        choice_1.save()

        choice_2 = Choice()
        choice_2.choice2 = 'False'
        choice_2.save()

        save_choice = Choice.objects.all()
        self.assertEqual(save_choice.count(), 2) 