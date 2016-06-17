from django.template import Library
from rango.models import Category
register=Library()

@register.inclusion_tag('rango/cats.html')
def get_category_list():
    return {'cats':Category.objects.all()}