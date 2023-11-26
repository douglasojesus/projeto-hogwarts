from django.shortcuts import render
from rest_framework import generics
from aluno.models import AlunoHogwarts as Aluno
from aluno.serializers import AlunoSerializer

class AlunoListCreateView(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class AlunoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer