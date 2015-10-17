from django.forms import ModelForm
from portal.models import Question
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS


class QuestionForm(ModelForm):
    class Meta:
		model = Question
		fields = ['question', 'keywords']
