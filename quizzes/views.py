from django.shortcuts import render, get_object_or_404
from .models import Quiz


def quiz_detail(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    return render(request, 'quizzes/detail.html', {'quiz': quiz})
