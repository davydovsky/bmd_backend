from rest_framework import serializers
from questionary import models


class QuestionaryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuestionaryStatus
        fields = '__all__'


class QuestionarySerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    questionary_status = QuestionaryStatusSerializer(read_only=True)

    class Meta:
        model = models.Questionary
        fields = '__all__'


class QuestionaryFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuestionaryFields
        fields = '__all__'


class DocumentTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DocumentTemplate
        fields = '__all__'
