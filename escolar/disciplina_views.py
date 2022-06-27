from django.shortcuts import render, redirect
from .models import Professor 

def dados(request, prof_matricula, disciplina_id):
    context = {'first_name': 'Johnny'}
    return render(request, 'professor_template/tab_disciplinas_dados.html', context)

def alunos(request, prof_matricula, disciplina_id):
    context = {'first_name': 'Johnny'}
    return render(request, 'professor_template/tab_disciplinas_alunos.html', context)

def aulas(request, prof_matricula, disciplina_id):
    context = {'first_name': 'Johnny'}
    return render(request, 'professor_template/tab_disciplinas_aulas.html', context)

def todas(request):
    context = {'first_name': 'Johnny'}
    return render(request, 'professor_template/disciplina.html', context)

def dados_disciplina(request, prof_matricula, disciplina_id):
    context = {'first_name': 'Johnny'}
    return render(request, 'professor_template/disciplina.html', context)

# Endpoint que busca todas as disciplinas de um professor
def disciplinas(request, prof_matricula):
    # database search
    # TODO implements
    context = {'first_name': 'Johnny'}
    return render(request, 'professor_template/disciplinas.html', context)

# Endpoint que busca os dados de uma disciplina de um professor
def disciplina_select(request, prof_id, disciplina_id):
    # database search
    # TODO implements
    context = {'first_name': 'Johnny'}
    return render(request, 'staff_template/staff_profile.html', context)

# Endpoint que retorna os alunos de uma disciplina
def disciplina_alunos(request, prof_id, disciplina_id):
    # database search
    # TODO implements
    context = {'first_name': 'Johnny'}
    return render(request, 'staff_template/staff_profile.html', context)
