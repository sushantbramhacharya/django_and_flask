from django.contrib import admin
from . import models
class ChoiceInline(admin.TabularInline):
    model = models.Choice
    extra = 1

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    # fields=["pub_date","question_text"]
    fieldsets = [
        ('Question info', {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines=[ChoiceInline]
    list_display =['pub_date','question_text','was_published_recently']
    list_editable=['question_text']
    list_filter=['pub_date','question_text']
    search_fields=['question_text']

# Order of fields in Django admin models 
# class ChoiceAdmin(admin.ModelAdmin):
#     fields=['votes','question','choice_text']

admin.site.register(models.Question,QuestionAdmin)
