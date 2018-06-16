
from django.urls import path
from Quiz import views
app_name = 'Quiz'
urlpatterns = [
   
    path('', views.home_page, name='home'),
    path('createquiz/', views.createquiz, name='createquiz'),
    path('goQuiz/', views.goQuiz, name='goQuiz'),
    path('<int:question_id>/detail/',views.detail, name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]