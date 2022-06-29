from django.db import models

# Create your models here.
##### Definição dos papéis no sistema
class Cadastro(models.Model):
    matricula = models.CharField(max_length=8, primary_key=True)
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=80,null=True)

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    carga_horaria = models.IntegerField(null=True)
    periodo = models.IntegerField(null=True)
    contagem_periodo= models.CharField(max_length=10, null=True)
    ano_oferta = models.IntegerField(null=True)

class Aluno(models.Model):
    cadastro_fk = models.OneToOneField(Cadastro, on_delete=models.CASCADE, primary_key=True)
    # ForeignKey define uma associação Um-para-Muitos
    # https://docs.djangoproject.com/en/3.2/ref/models/fields/#foreignkey
    curso_fk = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)
    serie = models.IntegerField(null=True)

class Servidor(models.Model):
    cadastro_fk = models.OneToOneField(Cadastro, on_delete=models.CASCADE)
    gestor = models.BooleanField()

class AreaConhecimento(models.Model):
    codigo = models.CharField(max_length=12, primary_key=True)
    descricao = models.CharField(max_length=200, null=True)

class Professor(models.Model):
    cadastro_fk = models.OneToOneField(Cadastro, on_delete=models.DO_NOTHING, primary_key=True)
    area_conhecimento_fk = models.ForeignKey(AreaConhecimento, on_delete=models.DO_NOTHING)

class Disciplina(models.Model):
    # O código pode ser de até 6 characteres. Por exemplo, Matemática pode ser MAT-S1, pois é do primeiro semestre
    codigo = models.CharField(max_length=6, primary_key=True)
    nome = models.CharField(max_length=200)
    area_conhecimento_fk = models.ForeignKey(AreaConhecimento, on_delete=models.DO_NOTHING)
    carga_horaria = models.IntegerField(null=True)
    curso_fk = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)
    # Removido pois já está no diário
    # professor_fk = models.OneToOneField(Professor, on_delete=models.DO_NOTHING)

class Diario(models.Model):
    disciplina_fk = models.ForeignKey(Disciplina, on_delete=models.DO_NOTHING)
    professor_fk = models.ForeignKey(Professor, on_delete=models.DO_NOTHING)
    inicio = models.DateField(null=True)
    fim = models.DateField(null=True)
    ano_semestre = models.CharField(max_length=5, null=True) #padrão: 2022_1

class Aula(models.Model):
    diario_fk = models.ForeignKey(Diario, on_delete=models.DO_NOTHING)
    ordem_aula = models.IntegerField(null=True)
    data_aula = models.DateField(null=True)
    descricao = models.CharField(max_length=300, null=True)

class DiarioAlunos(models.Model):
    diario_fk =  models.ForeignKey(Diario,  on_delete=models.DO_NOTHING)
    aluno_fk =  models.ForeignKey(Aluno,  on_delete=models.DO_NOTHING)
    # diario_fk =  models.ManyToManyField(Diario, on_delete=models.DO_NOTHING)
    # aluno_fk =  models.ManyToManyField(Aluno, on_delete=models.DO_NOTHING)

class FaltasDiario(models.Model):
    # diario_fk = models.OneToOneField(Diario, parent_link=True, on_delete=models.DO_NOTHING)
    # aluno_fk = models.OneToOneField(Aluno, parent_link=True, on_delete=models.DO_NOTHING)
    diario_alunos_fk = models.ForeignKey(DiarioAlunos, on_delete=models.DO_NOTHING)
    data_presenca = models.DateField(null=True) 
    presenca = models.BooleanField(null=True)
    