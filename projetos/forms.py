from django import forms  # Importa o módulo forms do Django para criar formulários
from .models import Projeto  # Importa o modelo Projeto para criar um formulário baseado nele
from datetime import date  # Importa a classe date para manipular datas

class ProjetoForm(forms.ModelForm):  # Define um formulário baseado no modelo Projeto
    class Meta:  # Define metadados para o formulário
        model = Projeto  # Especifica que o formulário será baseado no modelo Projeto
        fields = ['nome', 'descricao', 'responsavel', 'status', 'prazo']  # Define os campos do modelo que estarão no formulário

    def clean_nome(self):  # Método para validar o campo "nome"
        nome = self.cleaned_data['nome'].strip()  # Remove espaços extras do início e fim do nome
        if nome.lower().startswith('teste'):  # Verifica se o nome começa com "teste" (ignorando maiúsculas/minúsculas)
            raise forms.ValidationError('Nome não pode começar com "teste".')  # Lança um erro de validação
        return nome  # Retorna o nome validado

    def clean(self):  # Método para validações gerais do formulário
        data = super().clean()  # Chama o método clean da classe pai para obter os dados limpos
        prazo = data.get('prazo')  # Obtém o valor do campo "prazo"
        status = data.get('status')  # Obtém o valor do campo "status"
        if prazo and prazo < date.today():  # Verifica se o prazo está no passado
            self.add_error('prazo', 'Prazo não pode estar no passado.')  # Adiciona um erro ao campo "prazo"
        if status == 'concluido' and not data.get('descricao'):  # Verifica se o status é "concluído" e a descrição está vazia
            self.add_error('descricao', 'Descreva o que foi concluído.')  # Adiciona um erro ao campo "descricao"
        return data  # Retorna os dados validados
