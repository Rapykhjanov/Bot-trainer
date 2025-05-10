# urls.py (главный urls.py)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка Django
    path('api/', include('tasks.urls')),  # URL-ы вашего приложения (API)
]

# Замените 'your_app_name' на фактическое название вашего приложения,
# где находятся ваши views, serializers и urls.py.