from django.contrib import admin

from portal.models import Question

class QuestionAdmin(admin.ModelAdmin):
	list_display = ['question', 'keywords']
	class Meta:
		model = Question
admin.site.register(Question, QuestionAdmin)
