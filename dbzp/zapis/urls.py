from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

  path('', views.index, name='main'),
  path('add_discipline', views.add_discipline, name='adddisc'),
  path('notes', views.show_notes, name='notes'),
  path('notes/add_talon', views.add_note, name = 'add_note'),
  path('notes/add_talon/<int:note_id>', views.add_talon, name = 'add_talon'),
  path('notes/student_list', views.student_list, name = 'student_list')
]
