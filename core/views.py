from django.shortcuts import render


def home(request):
    """Landing page / home view."""
    return render(request, 'core/home.html')
