from rest_framework import generics, permissions, views, response, status
from questionary import models, serializers
from django.core.mail import send_mail
from django.conf import settings


class QuestionaryMixin:
    queryset = models.Questionary.objects.all()
    serializer_class = serializers.QuestionarySerializer
    permission_classes = (permissions.AllowAny,)


class QuestionaryListView(QuestionaryMixin, generics.ListCreateAPIView):
    pass


class QuestionaryDetailView(QuestionaryMixin, generics.RetrieveUpdateDestroyAPIView):
    pass


class QuestionaryStatusMixin:
    queryset = models.QuestionaryStatus.objects.all()
    serializer_class = serializers.QuestionaryStatusSerializer
    permission_classes = (permissions.AllowAny,)


class QuestionaryStatusListView(QuestionaryStatusMixin, generics.ListCreateAPIView):
    pass


class QuestionaryStatusDetailView(QuestionaryStatusMixin, generics.RetrieveUpdateDestroyAPIView):
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)

        if instance.status == models.QuestionaryStatus.RETURNED:
            send_mail(
                'Ваша анкета прокомментирована сотрудником',
                f'Ваша анкета прокомментирована сотрудником. '
                f'Перейдите по ссылке, чтобы внести изменения http://{settings.FRONTEND_IP}:8080/#/edit/{instance.questionary.pk}',
                settings.EMAIL_FROM,
                [instance.questionary.email]
            )
        return super().put(request, *args, **kwargs)


class QuestionaryFieldsMixin:
    queryset = models.QuestionaryFields.objects.all()
    serializer_class = serializers.QuestionaryFieldsSerializer
    permission_classes = (permissions.AllowAny,)


class QuestionaryFieldsListView(QuestionaryFieldsMixin, generics.ListCreateAPIView):
    pass


class QuestionaryFieldsDetailView(QuestionaryFieldsMixin, generics.RetrieveUpdateDestroyAPIView):
    pass


class DocumentTemplateMixin:
    queryset = models.DocumentTemplate.objects.all()
    serializer_class = serializers.DocumentTemplateSerializer


class DocumentTemplateListView(DocumentTemplateMixin, generics.ListCreateAPIView):
    pass


class DocumentTemplateDetailView(DocumentTemplateMixin, generics.RetrieveUpdateDestroyAPIView):
    pass


class DeleteAcceptedView(views.APIView):
    def delete(self, request, *args, **kwargs):
        models.Questionary.objects.delete_accepted()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class DeleteRejectedView(views.APIView):
    def delete(self, request, *args, **kwargs):
        models.Questionary.objects.delete_rejected()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
