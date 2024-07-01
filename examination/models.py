from datetime import datetime
from django.db import models
from django.utils import timezone

TEST_THEMAS= {
    ('animals','gyvunai'),
    ("KET", "keliu eimo taisykles"),
    ("flowers", "geles")
     }

class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Person(BaseModel):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_day = models.DateField(default=datetime(year=2000, month=1, day=1))

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.birth_day}'


class Exam(BaseModel):
    subject = models.CharField(max_length=200)
    topic = models.CharField(max_length=200, choices=TEST_THEMAS)

    def __str__(self):
        return f'{self.subject} {self.topic}'


class Question(BaseModel):
    complexity_level = {
        "1" : "easy",
        "2" : "medium",
        "3" : "hard",
    }
    question = models.CharField(max_length=200)
    complexity_level = models.CharField(max_length=200, choices=complexity_level, default='1')

    def __str__(self):
        return f'{self.question} {self.complexity_level}'


class PersonAnswer(BaseModel):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answers = models.CharField(max_length=200)
    correct = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.answers} {self.correct}'


class Result(BaseModel):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    answers_id = models.ForeignKey(PersonAnswer, on_delete=models.CASCADE)
    exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE)


class TestQuestion(BaseModel):
    test = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class ExamResult(BaseModel):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    test = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    question_answer = models.ForeignKey(PersonAnswer, on_delete=models.CASCADE)











