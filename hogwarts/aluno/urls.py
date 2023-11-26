from django.urls import path
from aluno.views import AlunoListCreateView, AlunoDetailView

urlpatterns = [
    path('alunos/', AlunoListCreateView.as_view(), name='item-list-create'),
    path('alunos/<int:pk>/', AlunoDetailView.as_view(), name='item-detail'),
]
