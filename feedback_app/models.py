# feedback_app/models.py
from django.db import models

class Feedback(models.Model):
    user_name = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_name} - {self.timestamp}'
