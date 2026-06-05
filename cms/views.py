from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def cms_home(request):
    """CMS hub — staff only."""
    return render(request, 'cms/home.html')
