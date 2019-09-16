from django.contrib import admin

from .models import Choice, Question


# class ChoiceInline(admin.StackedInline):
#    model = Choice
#    extra = 3


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # 自定义后台更改列表
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 过滤器
    list_filter = ['pub_date']
    # 搜索框
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
