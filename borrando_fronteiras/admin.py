from django.contrib import admin
from .models import BannerHero, SobreNos, Integrantes, EventosPublicacoes
from django_summernote.admin import SummernoteModelAdmin

@admin.register(BannerHero)
class BannerHeroAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(SobreNos)
class SobreNosAdmin(SummernoteModelAdmin):
    summernote_fields = ('conteudo',)
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(EventosPublicacoes)
class EventosPublicacoesAdmin(SummernoteModelAdmin):
    summernote_fields = ('conteudo',)
    list_display = ('nome_post', 'autor', 'criado')
    prepopulated_fields = {'slug': ['nome_post']}

@admin.register(Integrantes)
class IntegrantesAdmin(SummernoteModelAdmin):
    summernote_fields = ('conteudo',)
    list_display = ('nome_integrante',)
    prepopulated_fields = {'slug': ['nome_integrante']}