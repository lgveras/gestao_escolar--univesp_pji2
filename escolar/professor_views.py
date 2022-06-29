from django.shortcuts import render, redirect
from .models import Professor 

def home(request, prof_matricula):
    context = {
        'first_name': 'Johnny',
        'total_attendance': 10,
        'attendance_absent':4,
        'attendance_present': 4,
        'total_subjects': 8,
        'subject_name': 5,
        'data_present': [1,3,4,5],
        'data_absence': [2,3,5,4],
    }
    return render(request, 'professor_template/home.html', context)

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

