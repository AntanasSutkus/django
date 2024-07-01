from django.urls import path

from . import views

app_name = 'examination'

urlpatterns = [
    path("persons/", views.get_persons, name="persons"),
    path("persons/<int:pk>", views.get_person, name="person"),
    path("persons/<int:pk>/delete", views.delete_person, name="person_delete"),
    path("persons/<int:pk>/update", views.update_person, name="person_update"),
    path("persons/add", views.add_person, name="person_add"),
]


urlpatterns += [
    path("questions/", views.get_questions, name="questions"),
    path("questions/<int:pk>", views.get_question, name="question"),
    path("questions/add", views.add_question, name="question_add"),
    path("questions/<int:pk>/delete", views.delete_question, name="question_delete"),
    path("questions/<int:pk>/update", views.update_question, name="question_update")
]