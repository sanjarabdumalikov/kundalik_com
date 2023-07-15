from django.urls import path
from .views import (AllCreateSchoolView,DetailUpdateDeleteApiView)

urlpatterns = [
    path('school/',AllCreateSchoolView.as_view()),
    path('school/<pk>/',DetailUpdateDeleteApiView.as_view())
]