from django.urls import path
from . import views

app_name = 'modules'

urlpatterns = [
    path('<slug:slug>/', views.module_detail, name='detail'),
]
