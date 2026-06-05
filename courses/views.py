from django.shortcuts import render, get_object_or_404
from .models import Course


def course_list(request):
    courses = Course.objects.filter(is_published=True)
    return render(request, 'courses/list.html', {'courses': courses})


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug, is_published=True)
    modules = course.modules.all()
    return render(request, 'courses/detail.html', {'course': course, 'modules': modules})
