from django.db import models

# Create your models here.
##### Definição dos papéis no sistema
class Cadastro(models.Model):
    matricula = models.CharField(max_length=6, primary_key=True)
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    carga_horaria = models.IntegerField()
    periodo = models.IntegerField()
    contagem_periodo= models.CharField(max_length=10)
    ano_oferta = models.IntegerField()

class Aluno(models.Model):
    cadastro_fk = models.OneToOneField(Cadastro, on_delete=models.CASCADE)
    curso_fk = models.ForeignKey(Curso, on_delete=models.CASCADE)
    serie = models.IntegerField()

class Servidor(models.Model):
    cadastro_fk = models.OneToOneField(Cadastro, on_delete=models.CASCADE)
    gestor = models.BooleanField()

class AreaConhecimento(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    descricao = models.CharField(max_length=200)

class Professor(models.Model):
    cadastro_fk = models.OneToOneField(Cadastro, on_delete=models.DO_NOTHING)
    area_conhecimento_fk = models.OneToOneField(AreaConhecimento, on_delete=models.DO_NOTHING)

class Disciplina(models.Model):
    # O código pode ser de até 6 characteres. Por exemplo, Matemática pode ser MAT-S1, pois é do primeiro semestre
    codigo = models.CharField(max_length=6, primary_key=True)
    nome = models.CharField(max_length=200)
    area_conhecimento_fk = models.OneToOneField(AreaConhecimento, on_delete=models.DO_NOTHING)
    carga_horaria = models.IntegerField()
    curso_fk = models.OneToOneField(Curso, on_delete=models.DO_NOTHING)
    professor_fk = models.OneToOneField(Professor, on_delete=models.DO_NOTHING)

class Diario(models.Model):
    disciplina_fk = models.OneToOneField(Disciplina, on_delete=models.DO_NOTHING)
    professor_fk = models.OneToOneField(Professor, on_delete=models.DO_NOTHING)
    inicio = models.DateField()
    fim = models.DateField()
    ano_semestre = models.CharField(max_length=5) #padrão: 2022_1

class DiarioAlunos(models.Model):
    diario_fk =  models.OneToOneField(Diario, on_delete=models.DO_NOTHING)
    aluno_fk =  models.OneToOneField(Aluno, on_delete=models.DO_NOTHING)

class FaltasDiario(models.Model):
    # diario_fk = models.OneToOneField(Diario, parent_link=True, on_delete=models.DO_NOTHING)
    # aluno_fk = models.OneToOneField(Aluno, parent_link=True, on_delete=models.DO_NOTHING)
    diario_alunos_fk = models.OneToOneField(DiarioAlunos, on_delete=models.DO_NOTHING)
    data_presenca = models.DateField() 
    presenca = models.BooleanField()