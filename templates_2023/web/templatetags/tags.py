from django.template import Library

from templates_2023.web.views import Student

register = Library()


@register.simple_tag(name='student_info')
def show_student_info(student: Student):
    return f'Hello, my name is {student.name} and I am {student.age}-years old.'


@register.simple_tag(name='sample_tag')
def sample_tag(*args, **kwargs):
    return ', '.join(str (x) for x in (list(args) + list(kwargs.items())))

@register.inclusion_tag(name='nav')
def generate_nav(url_names)
