# CRUD Django básico (HTML)

## Passos
```bash
python -m venv .venv  # Cria um ambiente virtual para isolar as dependências do projeto
source .venv/bin/activate   # Ativa o ambiente virtual (Windows: .venv\Scripts\activate)
pip install -r requirements.txt  # Instala as dependências listadas no arquivo requirements.txt
python manage.py migrate  # Aplica as migrações para configurar o banco de dados
python manage.py createsuperuser  # Cria um usuário administrador para acessar o painel admin
python manage.py runserver  # Inicia o servidor de desenvolvimento do Django
```

- Acesse `/admin` para login.  # URL para acessar o painel administrativo do Django
- Acesse `/` para o CRUD.  # URL para acessar a aplicação CRUD

## Passo-a-passo para criar este projeto

1. **Criar o projeto Django**:
   ```bash
   django-admin startproject crudproj .
   ```
   - Isso cria a estrutura inicial do projeto Django.

2. **Criar a aplicação**:
   ```bash
   python manage.py startapp projetos
   ```
   - Isso cria a aplicação `projetos`, onde o CRUD será implementado.

3. **Configurar a aplicação no projeto**:
   - Adicione `'projetos'` à lista `INSTALLED_APPS` no arquivo `settings.py`.

4. **Criar o modelo**:
   - No arquivo `models.py` da aplicação `projetos`, defina o modelo `Projeto` com os campos necessários.
   - Exemplo:
     ```python
     class Projeto(models.Model):
         nome = models.CharField(max_length=120)
         descricao = models.TextField(blank=True)
         responsavel = models.CharField(max_length=80)
         status = models.CharField(max_length=12, choices=[('novo', 'Novo'), ('andamento', 'Em andamento'), ('concluido', 'Concluído')])
         prazo = models.DateField(null=True, blank=True)
     ```

5. **Criar e aplicar migrações**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
   - Isso cria e aplica as tabelas no banco de dados com base no modelo.

6. **Registrar o modelo no admin**:
   - No arquivo `admin.py`, registre o modelo para gerenciá-lo no painel administrativo:
     ```python
     from django.contrib import admin
     from .models import Projeto

     admin.site.register(Projeto)
     ```

7. **Criar as views**:
   - No arquivo `views.py`, implemente as views genéricas para listar, criar, atualizar e excluir projetos.

8. **Configurar as URLs**:
   - No arquivo `urls.py` da aplicação `projetos`, defina as rotas para as views:
     ```python
     from django.urls import path
     from . import views

     app_name = 'projetos'

     urlpatterns = [
         path('', views.ProjetoListView.as_view(), name='list'),
         path('novo/', views.ProjetoCreateView.as_view(), name='create'),
         path('<int:pk>/', views.ProjetoDetailView.as_view(), name='detail'),
         path('<int:pk>/editar/', views.ProjetoUpdateView.as_view(), name='update'),
         path('<int:pk>/excluir/', views.ProjetoDeleteView.as_view(), name='delete'),
     ]
     ```

9. **Criar os templates**:
   - Crie os arquivos HTML para listar, criar, editar e excluir projetos na pasta `templates/projetos`.

10. **Testar a aplicação**:
    - Execute o servidor de desenvolvimento:
      ```bash
      python manage.py runserver
      ```
    - Acesse as URLs `/` e `/admin` para verificar o funcionamento do CRUD e do painel administrativo.

## Configurações adicionais

### URL de Login
Adicione a seguinte configuração no arquivo `settings.py` para redirecionar usuários não autenticados para a página de login do admin:

```python
LOGIN_URL = '/admin/login/'
```

### Logout com método POST
Certifique-se de que o botão de logout no template utiliza um formulário com método `POST` para evitar erros de método não permitido (405):

```html
<form action="{% url 'logout' %}" method="post" style="display: inline;">
    {% csrf_token %}
    <button type="submit" style="background: none; border: none; color: blue; cursor: pointer; text-decoration: underline;">Sair</button>
</form>
```
