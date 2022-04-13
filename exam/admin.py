from django.contrib import admin
from .models import Question, Answer, Exam, ExamTimer


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ]


class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = [
        'answer_text',
        'is_right',
        'comment_for_right_answer',
        'comment_for_wrong_answer',
    ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'exam',
        'image',
    ]
    list_display = [
        'title',
        'exam',
        'date_updated',
    ]
    inlines = [
        AnswerInlineModel,
    ]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text',
        'is_right',
        'comment_for_right_answer',
        'comment_for_wrong_answer',
        'question',
    ]


@admin.register(ExamTimer)
class ExamTimerAdmin(admin.ModelAdmin):
    list_display = [
        'time_to_exam',
    ]
