from django.contrib.auth.mixins import LoginRequiredMixin  # Garante que apenas usuários autenticados acessem as views
from django.urls import reverse_lazy  # Gera URLs de forma preguiçosa, resolvendo-as apenas quando necessário
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView  # Views genéricas para operações CRUD
from django.db.models import Q  # Permite criar consultas complexas com condições "OU"
from django.contrib import messages  # Exibe mensagens de feedback ao usuário

from .models import Projeto  # Importa o modelo Projeto
from .forms import ProjetoForm  # Importa o formulário personalizado para o modelo Projeto

class ProjetoListView(LoginRequiredMixin, ListView):
    model = Projeto  # Modelo associado à view
    paginate_by = 10  # Número de itens por página
    template_name = 'projetos/projeto_list.html'  # Template usado para renderizar a lista

    def get_queryset(self):
        queryset = super().get_queryset()  # Obtém o queryset padrão
        termo_busca = self.request.GET.get('q', '').strip()  # Obtém o termo de busca da URL
        filtro_status = self.request.GET.get('status', '').strip()  # Obtém o filtro de status da URL

        if termo_busca:  # Aplica filtro de busca se fornecido
            queryset = queryset.filter(
                Q(nome__icontains=termo_busca) | Q(responsavel__icontains=termo_busca)  # Busca por nome ou responsável
            )
        if filtro_status:  # Aplica filtro de status se fornecido
            queryset = queryset.filter(status=filtro_status)

        return queryset  # Retorna o queryset filtrado

class ProjetoDetailView(LoginRequiredMixin, DetailView):
    model = Projeto  # Modelo associado à view
    template_name = 'projetos/projeto_detail.html'  # Template usado para exibir detalhes do projeto

class ProjetoCreateView(LoginRequiredMixin, CreateView):
    model = Projeto  # Modelo associado à view
    form_class = ProjetoForm  # Formulário usado para criar um novo projeto
    template_name = 'projetos/projeto_form.html'  # Template usado para o formulário de criação
    success_url = reverse_lazy('projetos:list')  # URL de redirecionamento após criação bem-sucedida
    # https://docs.djangoproject.com/en/5.2/ref/urlresolvers/#reverse-lazy

    def form_valid(self, form):
        self._adicionar_mensagem_sucesso('Projeto criado com sucesso.')  # Adiciona mensagem de sucesso
        return super().form_valid(form)  # Salva o objeto e redireciona

    def _adicionar_mensagem_sucesso(self, mensagem):
        messages.success(self.request, mensagem)  # Exibe mensagem de sucesso

class ProjetoUpdateView(LoginRequiredMixin, UpdateView):
    model = Projeto  # Modelo associado à view
    form_class = ProjetoForm  # Formulário usado para atualizar um projeto existente
    template_name = 'projetos/projeto_form.html'  # Template usado para o formulário de atualização
    success_url = reverse_lazy('projetos:list')  # URL de redirecionamento após atualização bem-sucedida

    def form_valid(self, form):
        self._adicionar_mensagem_sucesso('Projeto atualizado com sucesso.')  # Adiciona mensagem de sucesso
        return super().form_valid(form)  # Salva as alterações e redireciona

    def _adicionar_mensagem_sucesso(self, mensagem):
        messages.success(self.request, mensagem)  # Exibe mensagem de sucesso

class ProjetoDeleteView(LoginRequiredMixin, DeleteView):
    model = Projeto  # Modelo associado à view
    template_name = 'projetos/projeto_confirm_delete.html'  # Template usado para confirmar exclusão
    success_url = reverse_lazy('projetos:list')  # URL de redirecionamento após exclusão bem-sucedida

    def delete(self, request, *args, **kwargs):
        self._adicionar_mensagem_sucesso('Projeto excluído com sucesso.')  # Adiciona mensagem de sucesso
        return super().delete(request, *args, **kwargs)  # Realiza a exclusão e redireciona

    def _adicionar_mensagem_sucesso(self, mensagem):
        messages.success(self.request, mensagem)  # Exibe mensagem de sucesso
