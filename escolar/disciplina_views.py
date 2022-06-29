from types import NoneType
from django.shortcuts import render, redirect

from .models import Aula, Diario, DiarioAlunos, Disciplina, FaltasDiario, Professor

def dados(request, prof_matricula, disciplina_id):
    disciplina = Disciplina.objects.get(codigo=disciplina_id)
    professor = Professor.objects.get(cadastro_fk=prof_matricula)
    context = {
        'disciplina': disciplina,
        'professor': professor
    }
    return render(request, 'professor_template/tab_disciplinas_dados.html', context)

def alunos(request, prof_matricula, disciplina_id):
    disciplina = Disciplina.objects.get(codigo=disciplina_id)
    professor = Professor.objects.get(cadastro_fk=prof_matricula)
    diario = Diario.objects.get(
        disciplina_fk=disciplina_id, professor_fk=prof_matricula)
    diario_alunos = DiarioAlunos.objects.filter(diario_fk = diario)
    #faltas_diario = FaltasDiario.objects.filter(diario_alunos_fk = diario_alunos)

    datas_faltas = []
    faltas_alunos = []

    for aluno in diario_alunos:
        faltas_alunos.append(FaltasDiario.objects.filter(diario_alunos_fk = aluno))
        
    datas_faltas = FaltasDiario.objects.filter(diario_alunos_fk = diario_alunos[0]).values('data_presenca')

    context = {
        'disciplina': disciplina,
        'professor': professor,
        'datas_faltas': datas_faltas,
        'faltas_alunos': faltas_alunos,
    }
    return render(request, 'professor_template/tab_disciplinas_alunos.html', context)

# para alterar uma presença, preciso de
## diario, aluno e data

def aulas(request, prof_matricula, disciplina_id):
    disciplina = Disciplina.objects.get(codigo=disciplina_id)
    professor = Professor.objects.get(cadastro_fk=prof_matricula)
    
    diario = Diario.objects.get(
        disciplina_fk=disciplina_id, professor_fk=prof_matricula)
    # diario = Diario.objects.get(disciplina_fk=disciplina_id)

    aulas = Aula.objects.filter(diario_fk=diario)
    # diario_alunos = DiarioAlunos.objects.get(diario_fk = diario.id)
    # faltas_diario = FaltasDiario.objects

    context = {
        'aulas': aulas,
        'qtd_aulas': aulas.count(),
        'disciplina': disciplina,
        'professor': professor
    }

    if request.method == "POST":
        content = request.POST.get('aula_content')
        date = request.POST.get('aula_date')
        aula = Aula.objects.create(diario_fk=diario)
        last_order_number = Aula.objects.filter(diario_fk=diario).order_by('-ordem_aula')[0]
        print(last_order_number)
        if type(last_order_number.ordem_aula) is NoneType:
            aula.ordem_aula = 1 
        else:
            aula.ordem_aula = last_order_number.ordem_aula + 1 

        aula.descricao = content
        aula.data_aula = date
        aula.save() 

        # Necessário criar uma linha para cada aluno da disciplina em FaltasDiario
        # 1: Recuperar todos os alunos da disciplina
        diario_alunos = DiarioAlunos.objects.filter(diario_fk=diario)
        # 2: Criar uma entrada para cada um em FaltasDiario
        for entrada_diario in diario_alunos:
            falta_dia_aula = FaltasDiario.objects.create(diario_alunos_fk = entrada_diario)
            falta_dia_aula.data_presenca = date
            falta_dia_aula.presenca = True
            falta_dia_aula.save()

    return render(request, 'professor_template/tab_disciplinas_aulas.html', context)
    
# def add_aula(request, prof_matricula, disciplina_id):
#     form = RegisterForm()
#     if request.method == "POST":
#         form = RegisterForm(request.POST) #if no files
#         if form.is_valid():
#             #do something if form is valid
#             Aula.objects.create()

#     return aulas(request, prof_matricula, disciplina_id)

def lista_disciplina(request, prof_matricula):
    diarios = Diario.objects.filter(professor_fk=prof_matricula)
    context = {
        'prof_diarios': diarios,
    }
    return render(request, 'professor_template/todas_disciplinas.html', context)
