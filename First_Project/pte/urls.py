from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, AnswerViewSet, ScoreViewSet

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'scores', ScoreViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
