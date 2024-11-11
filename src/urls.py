from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.hello_world, name="hello_world"),
    path('login/', views.login, name="login"),
    path('question/<int:id>/', views.get_question, name="get_question"),
    path('question/<int:id>/check/', views.check_answer, name="check_answer"),
    path('status/', views.get_status, name="get_status"),
]