import uuid
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.postgres import fields as pg_fields


class QuestionaryManager(BaseUserManager):
    def delete_accepted(self):
        self._delete_with_status(QuestionaryStatus.ACCEPTED)

    def delete_rejected(self):
        self._delete_with_status(QuestionaryStatus.REJECTED)

    def _delete_with_status(self, status):
        self.filter(questionary_status__status=status).delete()


class Questionary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='Тело анкеты')
    email = models.EmailField(blank=True)
    questionary = pg_fields.JSONField(verbose_name='Тело анкеты')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    modified_date = models.DateTimeField(auto_now=True,  verbose_name='Дата и время модификации')

    objects = QuestionaryManager()

    class Meta:
        db_table = 'questionary_questionary'


class QuestionaryStatus(models.Model):
    FILLED = 0
    RETURNED = 1
    ACCEPTED = 2
    REJECTED = 3
    STATUS_CHOICES = (
        (FILLED, 'Заполнена'),
        (RETURNED, 'Отправлена на перезаполнение'),
        (ACCEPTED, 'Принята'),
        (REJECTED, 'Отклонена'),
    )
    questionary = models.OneToOneField(
        Questionary, on_delete=models.CASCADE, related_name='questionary_status', verbose_name='Тело анкеты'
    )
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, verbose_name='Статус анкеты')
    comment = models.TextField(blank=True, verbose_name='Комментарий проверяющего')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    modified_date = models.DateTimeField(auto_now=True,  verbose_name='Дата и время модификации')

    class Meta:
        db_table = 'questionary_questionary_status'


class QuestionaryFields(models.Model):
    fields = pg_fields.JSONField(verbose_name='Поля анкеты')
    options = pg_fields.JSONField(verbose_name='Справочники')

    class Meta:
        db_table = 'questionary_questionary_fields'


class DocumentTemplate(models.Model):
    name = models.CharField(max_length=1024)
    template = models.TextField(blank=True)

    class Meta:
        db_table = 'questionary_document_template'
