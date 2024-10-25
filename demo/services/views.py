from django.core.paginator import Paginator
from django.shortcuts import render

from main.models import Service

# Create your views here.
def services(request, services_slug=None):
    services = Service.objects.all()

    paginator = Paginator(services,6)
    page = request.GET.get('page', 1)

    current_page = paginator.page(int(page))

    context = {
        'services': current_page,
        "slug_url": services_slug
    }
  
    return render(request,'services/services.html', context)

def service(request, service_slug):
    service = Service.objects.get(slug=service_slug)

    context = {'service': service}

    return render(request,'services/service.html', context)
