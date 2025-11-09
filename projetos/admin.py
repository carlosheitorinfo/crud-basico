from django.contrib import admin
from .models import Projeto

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'responsavel', 'status', 'prazo', 'criado_em')
    search_fields = ('nome', 'responsavel')
    list_filter = ('status',)
