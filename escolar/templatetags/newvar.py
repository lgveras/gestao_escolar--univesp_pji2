from django import template

register = template.Library()

@register.simple_tag
def newvar():   
    lista_alunos = [
        {"nome": 'Alessandro', "idade": '17 anos'},
        {"nome": 'Marcia', "idade": '17 anos'},
        {"nome": 'Kassandra', "idade": '17 anos'}
    ]
    return lista_alunos