from django.shortcuts import render

from .models import Service


# Create your views here.
def services(request):
    # obtener los servicos de la BD y enviar el context con la informacion
    services = Service.objects.all()
    return render(request, template_name='services/services.html', context={'services': services})
