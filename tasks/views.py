# views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User, Question, Answer, Hint, TestResult, Subscription, PromoCode, Level, Topic
from .serializers import UserSerializer, QuestionSerializer, AnswerSerializer, HintSerializer, TestResultSerializer, SubscriptionSerializer, PromoCodeSerializer, LevelSerializer, TopicSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def register(self, request):
        """Регистрация пользователя."""
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #   @action(detail=False, methods=['post'])  #TODO:  login
    #   def login(self, request):
    #       """Аутентификация пользователя."""
    #       pass  # Реализуйте логику аутентификации


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    #   @action(detail=False, methods=['get'])  #TODO:  get_questions_by_topic_and_difficulty
    #   def get_questions_by_topic_and_difficulty(self, request):
    #       """Получение вопросов по теме и сложности."""
    #       pass  # Реализуйте фильтрацию


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    #   @action(detail=False, methods=['post'])   #TODO:  check_answer
    #   def check_answer(self, request):
    #       """Проверка ответа пользователя."""
    #       pass  # Реализуйте логику проверки ответа


class HintViewSet(viewsets.ModelViewSet):
    queryset = Hint.objects.all()
    serializer_class = HintSerializer


class TestResultViewSet(viewsets.ModelViewSet):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer

    #   @action(detail=False, methods=['get'])  #TODO:  get_user_results
    #   def get_user_results(self, request):
    #       """Получение результатов тестов пользователя."""
    #       pass  # Реализуйте получение результатов


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    #   @action(detail=False, methods=['post'])  #TODO:  create_subscription
    #   def create_subscription(self, request):
    #       """Создание подписки."""
    #       pass  # Реализуйте логику создания подписки


class PromoCodeViewSet(viewsets.ModelViewSet):
    queryset = PromoCode.objects.all()
    serializer_class = PromoCodeSerializer

    #   @action(detail=False, methods=['post'])  #TODO:  validate_promo_code
    #   def validate_promo_code(self, request):
    #       """Проверка и применение промокода."""
    #       pass  # Реализуйте логику проверки промокода


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer