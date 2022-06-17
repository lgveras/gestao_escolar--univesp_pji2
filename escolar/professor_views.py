from django.shortcuts import render, redirect

def home(request, prof_id):
    context = {'first_name': 'Johnny'}
    return render(request, 'professor_template/base_template.html', context)

def profile(request, prof_id):
    context = {'first_name': 'Johnny'}
    return render(request, 'professor_template/base_template.html', context)

# Endpoint que busca todas as disciplinas de um professor
def disciplinas(request, prof_id):
    # database search
    # TODO implements
    context = {'first_name': 'Johnny'}
    return render(request, 'staff_template/staff_profile.html', context)

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

