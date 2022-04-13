from rest_framework import serializers
from .models import Exam, Question, Answer, ExamTimer


class ExamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exam
        fields = [
            'title',
        ]


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:

        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
            'comment_for_right_answer',
            'comment_for_wrong_answer',
        ]


class RandomQuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:

        model = Question
        fields = [
            'title', 'answer',
        ]


class QuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    exam = ExamSerializer(read_only=True)

    class Meta:

        model = Question
        fields = [
            'exam', 'title', 'answer',
        ]


class ExamTimerSerializer(serializers.ModelSerializer):

    class Meta:

        model = ExamTimer
        fields = [
            'time_to_exam',
        ]
