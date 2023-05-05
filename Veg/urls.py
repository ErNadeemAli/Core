from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('student/',get_student,name='student'),
    path('check_marks/<studentid>',check_marks,name='marks'),
    path('top-student',get_top,name='top')
]
