from django import template

register = template.Library()


@register.simple_tag(name="all_recipes")
def show_all_recipes():
    pass
