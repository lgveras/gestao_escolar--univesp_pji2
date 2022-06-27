from django.shortcuts import render, redirect
from .models import Professor 

def home(request, prof_matricula):
    context = {'first_name': 'Johnny'}
    return render(request, 'professor_template/base_template.html', context)

def profile(request, prof_matricula):
    # ETAPAS DE PROFILE
    # 1. Buscar dados pelo model de Professor
    professor = Professor.objects.get(cadastro_fk=prof_matricula)
    # 2. Preencher o context
    context = {
        'prof_matricula': professor.cadastro_fk.matricula,
        'prof_nome': professor.cadastro_fk.nome,
        'prof_email': professor.cadastro_fk.email,
        'prof_telefone': professor.cadastro_fk.telefone,
        'prof_area': professor.area_conhecimento_fk.descricao,
    }
    # 3. Passar para o template do profile
    return render(request, 'professor_template/profile.html', context)

