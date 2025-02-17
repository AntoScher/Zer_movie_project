import os
import django

# Установите переменную окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_project.settings')

# Настройте Django
django.setup()

# Импортируйте функцию send_mail
from django.core.mail import send_mail

# Отправьте тестовое письмо
send_mail(
    'Test Email',
    'This is a test email.',
    'from@outlook.com',
    ['to@example.com'],
    fail_silently=False,
)
