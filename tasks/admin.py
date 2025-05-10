# admin.py
from django.contrib import admin
from .models import User, Question, Answer, Hint, TestResult, Subscription, PromoCode, Level, Topic

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'fio', 'phone_number', 'level', 'points')
    search_fields = ('fio', 'phone_number')
    list_filter = ('level',)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('topic_id', 'name')
    search_fields = ('name',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'text', 'topic', 'difficulty', 'subject')
    search_fields = ('text',)
    list_filter = ('topic', 'difficulty', 'subject')
    raw_id_fields = ('topic',)  # Улучшает производительность при большом количестве тем


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_id', 'question', 'user', 'is_correct', 'created_at')
    list_filter = ('is_correct', 'created_at')
    raw_id_fields = ('question', 'user')


@admin.register(Hint)
class HintAdmin(admin.ModelAdmin):
    list_display = ('hint_id', 'question', 'text')
    raw_id_fields = ('question',)


@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = ('test_result_id', 'user', 'start_time', 'end_time', 'correct_answers', 'incorrect_answers')
    list_filter = ('user', 'start_time', 'end_time')
    raw_id_fields = ('user',)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('subscription_id', 'user', 'start_date', 'end_date', 'is_active')
    list_filter = ('is_active', 'start_date', 'end_date')
    raw_id_fields = ('user',)


@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('promo_code_id', 'code', 'discount_type', 'expiry_date', 'is_used')
    list_filter = ('is_used', 'expiry_date')
    search_fields = ('code',)


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('level_id', 'name', 'required_points', 'description')
    search_fields = ('name',)