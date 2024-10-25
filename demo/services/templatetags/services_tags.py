from django import template
from django.utils.http import urlencode

from main.models import Service

register = template.Library()

@register.simple_tag()
def tag_services():
    return Service.objects.all()

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)