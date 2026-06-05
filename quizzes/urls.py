from django.urls import path
from . import views

app_name = 'quizzes'

urlpatterns = [
    path('<int:pk>/', views.quiz_detail, name='detail'),
]
