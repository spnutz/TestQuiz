from django.template.loader import render_to_string
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from Quiz.views import home_page
from Quiz.models import Question

class HomePageTest(TestCase):
    def teat_root_url_reolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

class QuestionModel(TestCase):
    def test_can_save_model(self):
        frist_question = Question()
        frist_question.question = ' Dog is animal ?'
        frist_question.save()

        first_ans = Question()
        first_ans.ans = 'True'
        first_ans.save()

        save_question = Question.objects.all()
        self.assertEqual(save_question.count(), 1)

        save_ans = Question.objects.all()
        self.assertEqual(save_ans.count(), 1)
