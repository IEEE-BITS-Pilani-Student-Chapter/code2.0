from django.contrib import admin
from .models import Question, Participant, Solution

admin.site.register(Participant)
admin.site.register(Question)
admin.site.register(Solution)