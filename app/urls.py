from django.urls import path
from app.views import *

urlpatterns = [
    path('', home, name="home"),
    path('logout/', logout_view, name="logout"),
    path('ques/', question_view, name="ques"),
    path('ques/<int:pk>/', solution, name="solution"),
]
