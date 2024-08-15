from rest_framework import serializers
from .models import Question, SummarizeSpokenText, ReOrderParagraph, ReadingMultipleChoice, Answer, Score

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title', 'question_type']

class QuestionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['user', 'question', 'answer_data']

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['answer', 'component_scores']
