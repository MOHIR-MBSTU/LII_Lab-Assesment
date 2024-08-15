from rest_framework import viewsets
from .models import Question, Answer, Score
from .serializers import QuestionSerializer, AnswerSerializer, ScoreSerializer
from rest_framework.response import Response
from rest_framework import status
import random

class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return QuestionDetailSerializer
        return super().get_serializer_class()

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        answer = self.get_object()

        # Implement scoring based on question type
        if answer.question.question_type == 'SST':
            score = {
                'Content': random.randint(0, 2),
                'Form': random.randint(0, 2),
                'Grammar': random.randint(0, 2),
                'Vocabulary': random.randint(0, 2),
                'Spelling': random.randint(0, 2),
            }
        elif answer.question.question_type == 'RO':
            # Implement RO scoring logic
            pass
        elif answer.question.question_type == 'RMMCQ':
            # Implement RMMCQ scoring logic
            pass

        # Save the score
        Score.objects.create(answer=answer, component_scores=score)

        return Response({'score': score}, status=status.HTTP_201_CREATED)

class ScoreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
