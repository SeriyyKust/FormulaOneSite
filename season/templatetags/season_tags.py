from django import template
from season.models import *

register = template.Library()

@register.inclusion_tag('season/list_teams.html')
def show_teams(sort=None, t_selected=0):
    if not sort:
        teams = Teams.objects.all()
    else:
        teams = Teams.objects.order_by(sort)

    return {'teams': teams, 't_selected': t_selected}