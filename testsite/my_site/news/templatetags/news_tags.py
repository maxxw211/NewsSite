from django import template
from news.models import Category

register = template.Library()


@register.simple_tag(name='data_list_categories')
def data_categories():
    return Category.objects.all()
