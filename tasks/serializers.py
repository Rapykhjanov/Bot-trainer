from rest_framework import serializers
from .models import User, Question, Answer, Hint, TestResult, Subscription, PromoCode, Level, Topic


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(read_only=True)
    level = LevelSerializer(read_only=True)

    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class HintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hint
        fields = '__all__'


class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class PromoCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoCode
        fields = '__all__'


class AnswerSubmitSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    question_id = serializers.IntegerField()
    answer_text = serializers.CharField(max_length=255)
