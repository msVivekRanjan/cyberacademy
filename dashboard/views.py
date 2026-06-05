from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile
from dashboard.models import Progress
from courses.models import Course


@login_required
def dashboard_home(request):
    """Main dashboard for authenticated users."""
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    progress, _ = Progress.objects.get_or_create(user=request.user)
    recent_courses = Course.objects.filter(is_published=True)[:4]

    context = {
        'profile': profile,
        'progress': progress,
        'recent_courses': recent_courses,
    }
    return render(request, 'dashboard/index.html', context)
