from django.test import TestCase  # Classe base para criar testes automatizados no Django
from django.urls import reverse  # Função para gerar URLs com base nos nomes das rotas
from django.contrib.auth import get_user_model  # Função para obter o modelo de usuário ativo
from datetime import date, timedelta  # Classes para manipular datas
from .models import Projeto  # Importa o modelo Projeto para criar e verificar objetos durante os testes

User = get_user_model()  # Obtém o modelo de usuário ativo

class ProjetoTests(TestCase):  # Define uma classe de testes para o modelo Projeto
    def setUp(self):
        self.user = User.objects.create_user('ricardo', 'r@example.com', 'senha123')  # Cria um usuário para os testes
        self.client.login(username='ricardo', password='senha123')  # Faz login com o usuário criado

    def test_create_view(self):
        resp = self.client.post(reverse('projetos:create'), {  # Envia uma requisição POST para criar um projeto
            'nome': 'Plataforma X',
            'descricao': 'MVP',
            'responsavel': 'Time A',
            'status': 'novo',
            'prazo': date.today() + timedelta(days=7)  # Define o prazo como 7 dias a partir de hoje
        })
        self.assertEqual(resp.status_code, 302)  # Verifica se o redirecionamento ocorreu (código 302)
        self.assertTrue(Projeto.objects.filter(nome='Plataforma X').exists())  # Verifica se o projeto foi criado

    def test_validation_nome(self):
        resp = self.client.post(reverse('projetos:create'), {  # Envia uma requisição POST com um nome inválido
            'nome': 'teste-qualquer',
            'descricao': 'x',
            'responsavel': 'y',
            'status': 'novo'
        })
        self.assertEqual(resp.status_code, 200)  # Verifica se a resposta foi renderizada (código 200)
        self.assertContains(resp, 'Nome não pode começar')  # Verifica se a mensagem de erro foi exibida

    def test_list_filter(self):
        Projeto.objects.create(nome='API A', responsavel='Ana', status='novo')  # Cria um projeto com status "novo"
        Projeto.objects.create(nome='Web B', responsavel='Bruno', status='andamento')  # Cria um projeto com status "andamento"
        url = reverse('projetos:list') + '?q=API&status=novo'  # Gera a URL com parâmetros de busca e filtro
        resp = self.client.get(url)  # Envia uma requisição GET para a lista de projetos
        self.assertContains(resp, 'API A')  # Verifica se o projeto "API A" está na resposta
        self.assertNotContains(resp, 'Web B')  # Verifica se o projeto "Web B" não está na resposta
