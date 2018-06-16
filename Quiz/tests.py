from django.template.loader import render_to_string
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from Quiz.views import home_page
from Quiz.models import Question, Choice
from selenium import webdriver 

class HomePageTest(TestCase):
    def teat_root_url_reolve_to_home_page_view(self):
        found = resolve('/quiz/')
        self.assertEqual(found.func, home_page)

    def test_home_page_can_use(self):
        response = self.client.get('/quiz/')
        self.assertTemplateUsed(response, 'home.html')


class CreateChoicePageTest(TestCase):
    def test_create_choice_page(self):
        response = self.client.get('/quiz/createquiz/')
        self.assertTemplateUsed(response, 'createquiz.html')


    def test_show_quiz_page(self):
        response = self.client.get('/quiz/goQuiz/')
        self.assertTemplateUsed(response, 'answer.html')

   






class itemModel(TestCase):
    def test_can_save_model_question(self):
        frist_item = Question()
        frist_item.question_text = 'Dog is animal'
        frist_item.ans = 'True'
        frist_item.save()

        second_item = Question()
        second_item.question_text = 'cat is dog'
        second_item.ans='False'
        second_item.save()

        save_item = Question.objects.all()
        self.assertEqual(save_item.count(), 2)

        self.assertEqual(save_item[0].question_text, 'Dog is animal')
        self.assertEqual(save_item[0].ans, 'True')

        self.assertEqual(save_item[1].question_text, 'cat is dog')
        self.assertEqual(save_item[1].ans, 'False')

        
    def test_can_save_model_choice(self):
        list_choice = Question()
        list_choice.save()

        item_choice = Choice()
        item_choice.choice1 = 'True'
        item_choice.choice2 = 'False'
        item_choice.question = list_choice
        item_choice.save()


        save_choice = Choice.objects.all()
        self.assertEqual(save_choice.count(),1)
        self.assertEqual(save_choice[0].choice1, 'True')
        self.assertEqual(save_choice[0].choice2, 'False')
       

       

       
