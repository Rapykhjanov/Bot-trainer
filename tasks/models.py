from django.db import models
from django.utils import timezone


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    fio = models.CharField(max_length=255, verbose_name="ФИО")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    level = models.IntegerField(default=1, verbose_name="Уровень")
    points = models.IntegerField(default=0, verbose_name="Баллы")

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Название темы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"


class Level(models.Model):
    level_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Название уровня")
    required_points = models.IntegerField(verbose_name="Необходимое количество баллов")
    description = models.TextField(verbose_name="Описание уровня")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Уровень"
        verbose_name_plural = "Уровни"


class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    text = models.TextField(verbose_name="Текст вопроса")
    image_url = models.URLField(null=True, blank=True, verbose_name="URL изображения")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name="Тема")
    difficulty = models.CharField(max_length=50, verbose_name="Сложность")
    subject = models.CharField(max_length=100, verbose_name="Предмет")
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Уровень сложности")

    def __str__(self):
        return f"Вопрос {self.question_id} ({self.topic})"

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Вопрос", related_name="answer_set")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    text = models.CharField(max_length=255, verbose_name="Текст ответа")
    is_correct = models.BooleanField(default=False, verbose_name="Правильный ответ")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата и время ответа")

    def __str__(self):
        return f"Ответ на {self.question} от {self.user}"

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"


class Hint(models.Model):
    hint_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Вопрос")
    text = models.TextField(verbose_name="Текст подсказки")
    image_url = models.URLField(null=True, blank=True, verbose_name="URL изображения подсказки")

    def __str__(self):
        return f"Подсказка к {self.question}"

    class Meta:
        verbose_name = "Подсказка"
        verbose_name_plural = "Подсказки"


class TestResult(models.Model):
    test_result_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    start_time = models.DateTimeField(verbose_name="Время начала теста", default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True, verbose_name="Время окончания теста")
    correct_answers = models.IntegerField(default=0, verbose_name="Правильные ответы")
    incorrect_answers = models.IntegerField(default=0, verbose_name="Неправильные ответы")

    def __str__(self):
        return f"Результат теста {self.test_result_id} пользователя {self.user}"

    class Meta:
        verbose_name = "Результат теста"
        verbose_name_plural = "Результаты тестов"


class Subscription(models.Model):
    subscription_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    start_date = models.DateField(verbose_name="Дата начала подписки")
    end_date = models.DateField(verbose_name="Дата окончания подписки")
    is_active = models.BooleanField(default=True, verbose_name="Активна")

    def __str__(self):
        return f"Подписка пользователя {self.user}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"


class PromoCode(models.Model):
    promo_code_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50, unique=True, verbose_name="Код")
    discount_type = models.CharField(max_length=100, verbose_name="Тип скидки")
    expiry_date = models.DateField(null=True, blank=True, verbose_name="Дата истечения")
    is_used = models.BooleanField(default=False, verbose_name="Использован")

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Промокод"
        verbose_name_plural = "Промокоды"
