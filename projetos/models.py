from django.db import models  # Importa o módulo models para definir os modelos do banco de dados
from django.core.validators import MinLengthValidator  # Importa um validador para garantir o tamanho mínimo de campos

class Projeto(models.Model):  # Define a classe Projeto, que representa uma tabela no banco de dados
    STATUS = [  # Define as opções de status como uma lista de tuplas
        ('novo', 'Novo'),  # Opção "novo" com o rótulo "Novo"
        ('andamento', 'Em andamento'),  # Opção "andamento" com o rótulo "Em andamento"
        ('concluido', 'Concluído'),  # Opção "concluido" com o rótulo "Concluído"
    ]

    nome = models.CharField(  # Define um campo de texto com tamanho máximo para o nome do projeto
        max_length=120,  # Limita o tamanho máximo do texto a 120 caracteres
        unique=True,  # Garante que o nome seja único no banco de dados
        validators=[MinLengthValidator(3)]  # Valida que o nome tenha pelo menos 3 caracteres
    )
    descricao = models.TextField(blank=True)  # Campo de texto longo para a descrição, opcional (pode ser vazio)
    responsavel = models.CharField(max_length=80)  # Campo de texto para o nome do responsável, com limite de 80 caracteres
    status = models.CharField(  # Campo de texto para armazenar o status do projeto
        max_length=12,  # Limita o tamanho máximo do texto a 12 caracteres
        choices=STATUS,  # Define as opções disponíveis para o status
        default='novo'  # Define "novo" como valor padrão
    )
    prazo = models.DateField(null=True, blank=True)  # Campo de data para o prazo, opcional (pode ser nulo ou vazio)
    criado_em = models.DateTimeField(auto_now_add=True)  # Armazena a data e hora de criação automaticamente
    atualizado_em = models.DateTimeField(auto_now=True)  # Armazena a data e hora da última atualização automaticamente

    class Meta:  # Define metadados para o modelo
        ordering = ['-criado_em']  # Ordena os projetos pela data de criação em ordem decrescente

    def __str__(self):  # Define a representação em string do objeto
        return self.nome  # Retorna o nome do projeto como representação textual
