from django.db import models
from django.contrib.auth.models import User
#from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class BannerHero(models.Model):
    imagem = models.ImageField(null=True, blank=True, verbose_name='Imagem', help_text='Tamanho para ser usado: 1169x1136px')

    class Meta:
        verbose_name = 'Conteúdo'
        verbose_name_plural = 'Banner Hero'
    
    titulo_banner = 'Banner Hero'
    def __str__(self):  
        return self.titulo_banner

class SobreNos(models.Model):
    imagem = models.ImageField(null=True, blank=True, verbose_name='Imagem', help_text='Tamanho recomendado da imagem: 576x411px')
    conteudo = models.TextField(verbose_name='Conteúdo')

    titulo_sobre = 'Sobre Nós'
    def __str__(self):  
        return self.titulo_sobre

    class Meta:
        verbose_name = 'Conteúdo'
        verbose_name_plural = 'Sobre Nós'
    

class Integrantes(models.Model):
    nome_integrante = models.CharField(max_length=100, verbose_name='Nome do Integrante')
    slug = models.SlugField(max_length=255, unique=True, blank=True, verbose_name='Slug')
    imagem = models.ImageField(null=True, blank=True, upload_to='integrantes', verbose_name='Imagem', help_text='Tamanho recomendado da imagem: 349x474px')
    conteudo = models.TextField(verbose_name='Conteúdo')
    
    def __str__(self):    
        return self.nome_integrante
    
    class Meta:
        verbose_name = 'Integrante'
        verbose_name_plural = 'Integrantes'
        ordering = ['slug']

    

class EventosPublicacoes(models.Model):
    nome_post = models.CharField(max_length=255, verbose_name='Nome do Post')
    slug = models.SlugField(max_length=255, unique=True, blank=True, verbose_name='Slug')
    imagem = models.ImageField(null=True, blank=True, upload_to='eventos_publicacoes', verbose_name='Imagem', help_text='Tamanho recomendado da imagem: 530x392px')
    conteudo = models.TextField(verbose_name='Conteúdo')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):  
        return self.nome_post

    class Meta:
        verbose_name = 'Evento e Publicação'
        verbose_name_plural = 'Eventos e Publicações'
        ordering = ['slug']
    
    
