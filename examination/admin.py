from django.contrib import admin

from .models import Person, Exam, Question, PersonAnswer, Result, TestQuestion


class ChoiceInline(admin.TabularInline):
    model = PersonAnswer
    extra = 4


class QuestionsAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


admin.site.register(Person)

admin.site.register(Exam)

admin.site.register(Question, QuestionsAdmin)

admin.site.register(PersonAnswer)

admin.site.register(Result)

admin.site.register(TestQuestion)






