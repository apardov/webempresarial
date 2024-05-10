from .models import Link


def context_dicctionary(request):
    social_context = {}
    links = Link.objects.all()
    for link in links:
        social_context[link.key] = link.url
    return social_context
