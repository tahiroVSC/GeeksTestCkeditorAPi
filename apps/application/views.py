from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from apps.application.serializers import ApplicationSerializers
from apps.application.models import Application
from django.core.mail import send_mail, EmailMessage
from Triatlon import settings

class ApplicationsAPIViews(ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        instance = serializer.instance
        name = instance.name
        number = instance.number
        email = instance.email
        summary = instance.summary if instance.summary else "Нет файла"
        
        subject = 'Оставлено заявление'
        message = f'Заявление:\n\nИмя: {name}\nНомер: {number}\nПочта: {email}'
        
        email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, ['topkek164@gmail.com'])
        email.attach(f'{name} - Резюме',f'{settings.BASE_DIR}/{summary}')
        email.send()
        # send_mail(
        #     subject,
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     ['topkek164@gmail.com'],
        #     fail_silently=False,
        # )

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)