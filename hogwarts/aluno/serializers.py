from rest_framework import serializers
from aluno.models import AlunoHogwarts as Aluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'