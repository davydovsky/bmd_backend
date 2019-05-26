from django.db.models.signals import post_save
from django.dispatch import receiver
from questionary import models


@receiver(post_save, sender=models.Questionary,)
def create_status(sender, instance, created, **kwargs):
    if created:
        models.QuestionaryStatus.objects.get_or_create(
            questionary=instance,
            status=models.QuestionaryStatus.FILLED
        )
    else:
        instance.questionary_status.status = models.QuestionaryStatus.FILLED
        instance.questionary_status.save()
