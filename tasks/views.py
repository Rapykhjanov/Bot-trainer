from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from .models import User, Question, Answer, Hint, TestResult, Subscription, PromoCode, Level, Topic, Theory, TrainingSession
from .serializers import UserSerializer, QuestionSerializer, AnswerSerializer, HintSerializer, TestResultSerializer, \
    SubscriptionSerializer, PromoCodeSerializer, LevelSerializer, TopicSerializer, AnswerSubmitSerializer, \
    TheorySerializer, TrainingSessionSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        topic_id = self.request.query_params.get('topic', None)
        level_id = self.request.query_params.get('level', None)

        if topic_id:
            queryset = queryset.filter(topic_id=topic_id)
        if level_id:
            queryset = queryset.filter(level_id=level_id)

        return queryset


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    @action(detail=True, methods=['post'])
    def check_answer(self, request, pk=None):
        answer = self.get_object()
        correct_answer = answer.question.answer_set.filter(is_correct=True).first()

        if answer.text == correct_answer.text:
            answer.is_correct = True
            answer.save()
            return Response({"message": "Правильный ответ!"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Неправильный ответ!"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def submit_answer(self, request):
        serializer = AnswerSubmitSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            question_id = serializer.validated_data['question_id']
            answer_text = serializer.validated_data['answer_text']

            user = User.objects.get(user_id=user_id)
            question = Question.objects.get(question_id=question_id)

            # Добавление ответа
            answer = Answer.objects.create(user=user, question=question, text=answer_text)
            # Проверка на правильность
            correct_answer = question.answer_set.filter(is_correct=True).first()
            if correct_answer.text == answer_text:
                answer.is_correct = True
                answer.save()
                return Response({"message": "Правильный ответ!"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Неправильный ответ!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HintViewSet(viewsets.ModelViewSet):
    queryset = Hint.objects.all()
    serializer_class = HintSerializer


class TestResultViewSet(viewsets.ModelViewSet):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer

    @action(detail=True, methods=['post'])
    def submit_test(self, request, pk=None):
        test_result = self.get_object()
        test_result.end_time = timezone.now()
        test_result.save()
        return Response({"message": "Результаты теста успешно отправлены!"}, status=status.HTTP_200_OK)


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    @action(detail=False, methods=['post'])
    def subscribe(self, request):
        user_id = request.data.get('user_id')
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')

        user = User.objects.get(user_id=user_id)
        subscription = Subscription.objects.create(user=user, start_date=start_date, end_date=end_date)
        subscription.save()

        return Response({"message": f"Подписка для пользователя {user.fio} активирована!"}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def active_subscriptions(self, request):
        active_subscriptions = Subscription.objects.filter(is_active=True)
        serializer = SubscriptionSerializer(active_subscriptions, many=True)
        return Response(serializer.data)


class PromoCodeViewSet(viewsets.ModelViewSet):
    queryset = PromoCode.objects.all()
    serializer_class = PromoCodeSerializer


class TheoryViewSet(viewsets.ModelViewSet):
    queryset = Theory.objects.all()
    serializer_class = TheorySerializer

    @action(detail=True, methods=['get'])
    def get_theory(self, request, pk=None):
        theory = self.get_object()
        serializer = TheorySerializer(theory)
        return Response(serializer.data)


class TrainingSessionViewSet(viewsets.ModelViewSet):
    queryset = TrainingSession.objects.all()
    serializer_class = TrainingSessionSerializer

    @action(detail=True, methods=['get'])
    def start_training(self, request, pk=None):
        session = self.get_object()
        # Логика для начала тренировки (например, определение сессии и заданий)
        return Response({"message": f"Тренировка {session.id} начата!"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def complete_training(self, request, pk=None):
        session = self.get_object()
        session.end_time = timezone.now()  # или другой логики завершения
        session.save()
        return Response({"message": f"Тренировка {session.id} завершена!"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def return_to_main(self, request):
        # Логика для возврата на главную страницу
        return Response({"message": "Вы вернулись на главную страницу!"}, status=status.HTTP_200_OK)