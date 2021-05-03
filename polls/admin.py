from django.contrib import admin

from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3

class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields': ['question_text']}),
    ('Date Information', {'fields': ['pub_date']}),
  ]
  # This tells Django: “Choice objects are edited on the Question admin page. By default, provide enough fields for 3 choices.”
  inlines = [ChoiceInline]
  list_display = ('question_text', 'pub_date', 'was_published_recently')
  list_filter = ['pub_date']

# Model Registration.
admin.site.register(Question, QuestionAdmin)
