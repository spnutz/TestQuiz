from django.template.loader import render_to_string
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from Quiz.views import home_page

class HomePageTest(TestCase):
    def teat_root_url_reolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

# Create your tests here.
