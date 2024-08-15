from django.test import TestCase
from rest_framework.test import APIClient
from .models import Question, Answer

class QuestionTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_list_questions(self):
        response = self.client.get('/api/questions/')
        self.assertEqual(response.status_code, 200)

    def test_submit_answer(self):
        question = Question.objects.create(title="Sample Question", question_type="SST")
        response = self.client.post('/api/answers/', {
            'user': 1,
            'question': question.id,
            'answer_data': {'text': 'Sample answer'}
        })
        self.assertEqual(response.status_code, 201)
