from datetime import datetime

from django import template

register = template.Library()


@register.filter('odd')
def get_odd(values):
    return [x for x in values if x % 2 == 1]


@register.filter('even')
def get_even(values):
    return [x for x in values if x % 2 == 0]


@register.filter('app_style')
def format_to_app_style(date):
    return date.strftime('%m/%d/%y')
