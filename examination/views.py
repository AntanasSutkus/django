from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Person, Question, TestQuestion
from .forms import PersonForm, QuestionForm
import json


def get_persons(request):
    persons = Person.objects.all()
    context = {"persons": persons}
    return render(request,"examination/persons.html", context)


def get_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    context = {"person": person, "pk": pk}
    return render(request,"examination/person.html", context)


def delete_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    context = {"person": person}
    if request.method == "POST":
        person.delete()
        return redirect("examination:persons")
    return render(request,"examination/person_delete.html", context)


def add_person(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('examination:persons')
    else:
        form =PersonForm()
    return render(request,"examination/person_add.html",{'form':form})


def update_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('examination:person', pk =pk)
    else:
        form = PersonForm(instance=person)
    context = {"form": form}
    return render(request, "examination/person_update.html",context)


def get_questions(request):
    questions = Question.objects.all()
    context = {"questions": questions}
    return render(request, "examination/questions.html", context)


def delete_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {"question": question}
    if request.method == "POST":
        question.delete()
        return redirect("examination:questions")
    return render(request,"examination/question_delete.html", context)


def add_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('examination:questions')
    else:
        form =QuestionForm()
    return render(request,"examination/question_add.html",{'form':form})


def get_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {"question": question, "pk": pk}
    return render(request,"examination/question.html", context)


def update_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('examination:questions')
    else:
        form = QuestionForm(instance=question)
    context = {"form": form}
    return render(request, "examination/question_update.html",context)

