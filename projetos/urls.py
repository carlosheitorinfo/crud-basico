from django.urls import path  # Importa a função path para definir rotas
from . import views  # Importa o módulo views da aplicação atual

app_name = 'projetos'  # Define um namespace para as URLs desta aplicação

urlpatterns = [
    path('', views.ProjetoListView.as_view(), name='list'),  # Rota para listar projetos
    # URL: '/' (raiz da aplicação)
    # View: ProjetoListView (exibe a lista de projetos)
    # name: 'list' (usado para referenciar esta rota nos templates e no código)

    path('novo/', views.ProjetoCreateView.as_view(), name='create'),  # Rota para criar um novo projeto
    # URL: '/novo/'
    # View: ProjetoCreateView (exibe o formulário para criar um novo projeto)
    # name: 'create'

    path('<int:pk>/', views.ProjetoDetailView.as_view(), name='detail'),  # Rota para exibir detalhes de um projeto
    # URL: '/<int:pk>/' (o <int:pk> é um parâmetro dinâmico que representa o ID do projeto)
    # View: ProjetoDetailView (exibe os detalhes de um projeto específico)
    # name: 'detail'

    path('<int:pk>/editar/', views.ProjetoUpdateView.as_view(), name='update'),  # Rota para editar um projeto
    # URL: '/<int:pk>/editar/'
    # View: ProjetoUpdateView (exibe o formulário para editar um projeto existente)
    # name: 'update'

    path('<int:pk>/excluir/', views.ProjetoDeleteView.as_view(), name='delete'),  # Rota para excluir um projeto
    # URL: '/<int:pk>/excluir/'
    # View: ProjetoDeleteView (exibe a confirmação para excluir um projeto)
    # name: 'delete'
]
