from django.shortcuts import render
from borrando_fronteiras.models import BannerHero, SobreNos, Integrantes, EventosPublicacoes

def Home(request):
    bannerHero = BannerHero.objects.get(pk=4)
    sobreNos = SobreNos.objects.get(pk=1)
    integrantesList = Integrantes.objects.all()
    eventosList = EventosPublicacoes.objects.all()
    return render(request, 'index.html', {'BannerHero': bannerHero,'SobreNos': sobreNos, 'Integrantes': integrantesList, 'EventosPublicacoes': eventosList})

def IntegrantesDetail(request, slug=None):
    template_integrante = 'pagina-integrante.html'
    integrante_item = Integrantes.objects.get(slug=slug)
    context = {'integrante': integrante_item}
    return render(request, template_integrante, context)

def EventosPublicacoesDetail(request, slug=None):
    template_evento = 'pagina-evento.html'
    evento_item = EventosPublicacoes.objects.get(slug=slug)
    context = {'evento': evento_item}
    return render(request, template_evento, context)

