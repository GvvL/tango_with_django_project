from rango.models import Category
from django.template import Library
register=Library()
@register.inclusion_tag('rango/cats.html')
def side_cats_tag(cat=None):
    return {'cats':Category.objects.all(),'act_cat':cat}