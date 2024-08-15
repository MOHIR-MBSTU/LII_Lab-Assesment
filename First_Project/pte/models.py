from django.db import models

class Question(models.Model):
    QUESTION_TYPES = [
        ('SST', 'Summarize Spoken Text'),
        ('RO', 'Re-Order Paragraph'),
        ('RMMCQ', 'Reading Multiple Choice Multiple'),
    ]
    title = models.CharField(max_length=255)
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES)

class SummarizeSpokenText(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    time_limit = models.IntegerField()
    audio_files = models.JSONField()  # Store list of audio file URLs with speaker info

class ReOrderParagraph(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    paragraphs = models.JSONField()  # Store unordered paragraphs

class ReadingMultipleChoice(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    passage = models.TextField()
    options = models.JSONField()  # Store options


from django.contrib.auth.models import User

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_data = models.JSONField()  # Store answer data depending on question type
    submitted_at = models.DateTimeField(auto_now_add=True)

class Score(models.Model):
    answer = models.OneToOneField(Answer, on_delete=models.CASCADE)
    component_scores = models.JSONField()  # Store scores for each component
