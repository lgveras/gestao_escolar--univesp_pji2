from asyncio.log import logger
from turtle import clear
from django.core.management.base import BaseCommand, CommandError
from psycopg2 import Date
from escolar.models import Aluno, Cadastro, Curso, Diario, DiarioAlunos, Professor, AreaConhecimento, Disciplina
import names
import datetime

# Exemplo de comando
# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "Seed do banco de gestão escolar"

    def add_arguments(self, parser) -> None:
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done!')


def run_seed(self, mode):
    if mode == MODE_REFRESH:
        create_data_in_tables()
    elif mode == MODE_CLEAR:
        clear_data_from_tables()


def create_data_in_tables():
    # É importante que a inserção dos dados siga a ordem abaixo devido às associações
    create_cadastro()
    create_areas_conhecimento()
    create_professor()
    create_curso()
    create_disciplina()
    create_diario()
    create_aluno()
    create_diarioalunos()


def clear_data_from_tables():
    # É importante que a inserção dos dados siga a ordem abaixo devido às associações
    clear_diarioalunos()
    clear_aluno()
    clear_diario()
    clear_disciplina()
    clear_curso()

    # Limpamos professor primeiro por causa das dependências
    clear_professor()
    clear_areaconhecimento()
    clear_cadastro()


def create_cadastro():
    logger.info("Criando dados da tabela 'cadastro'...")

    # Cadastro 1
    cad1 = Cadastro.objects.create(
        matricula="SERV-001",
        idade=30,
    )
    cad1.nome = "Marcelo Madureira"
    # cad1.idade = 30
    cad1.telefone = "(011)9999999"
    cad1.email = "marcelo@univesp.br"
    cad1.senha = "123"
    cad1.save()

    # Cadastro 2
    cad2 = Cadastro.objects.create(
        matricula="SERV-002",
        idade=28,
    )
    # cad2.matricula = "000002"
    cad2.nome = "Cassandra Marques"
    # cad1.idade = 28
    cad2.telefone = "(011)9999999"
    cad2.email = "cassa@univesp.br"
    cad2.senha = "123"

    cad2.save()

    # Cadastro 3
    cad3 = Cadastro.objects.create(
        matricula="SERV-003",
        idade=30,
    )
    # cad3.matricula = "000003"
    cad3.nome = "Tenorio Nunes"
    # cad1.idade = 40
    cad3.telefone = "(011)9999999"
    cad3.email = "tenorio@univesp.br"
    cad3.senha = "123"

    cad3.save()


def create_areas_conhecimento():
    # Tabela de áreas do conhecimento
    # http://lattes.cnpq.br/documents/11871/24930/TabeladeAreasdoConhecimento.pdf/d192ff6b-3e0a-4074-a74d-c280521bd5f7
    # ou http://fisio.icb.usp.br:4882/posgraduacao/bolsas/capesproex_bolsas/tabela_areas.html
    area1 = AreaConhecimento.objects.create(
        codigo="1.01.00.00-8"
    )
    # area1.codigo = "1.01.00.00-8"
    area1.descricao = "Matemática"
    area1.save()

    area2 = AreaConhecimento.objects.create(
        codigo="1.05.00.00-6 "
    )
    # area2.codigo = "1.05.00.00-6 "
    area2.descricao = "Física"
    area2.save()

    area3 = AreaConhecimento.objects.create(
        codigo="7.08.00.00-6"
    )
    # area2.codigo = "7.08.00.00-6"
    area3.descricao = "Educação"
    area3.save()


def create_professor():
    logger.info("Criando dados da tabela 'cadastro'...")

    cad1 = Cadastro.objects.get(matricula="SERV-002")
    ac1 = AreaConhecimento.objects.get(codigo="7.08.00.00-6")

    if cad1 and ac1:
        prof1 = Professor.objects.create(
            # Passar a instância ao invés do valor da chave de cadastro e area conhecimento
            cadastro_fk=cad1,
            area_conhecimento_fk=ac1
        )
        # prof1.cadastro_fk = cad1.matricula
        # prof1.area_conhecimento_fk = ac1.codigo
    else:
        logger.error(
            "Não foi possível encontrar um cadastro para associar ao professor")


def create_curso():
    logger.info("Criando dados da tabela 'curso'...")
    curso1 = Curso.objects.create()
    curso1.nome = "Ensino Médio"
    curso1.descricao = " Descrição do Ensino Médio"
    curso1.carga_horaria = 2000
    curso1.periodo = 3
    curso1.contagem_periodo = "Ano"
    curso1.ano_oferta = 2022
    curso1.save()


def create_disciplina():
    logger.info("Criando dados da tabela 'disciplina'...")
    disciplina1 = Disciplina.objects.create(
        codigo="MAT-3A",
        area_conhecimento_fk=AreaConhecimento.objects.get(
            codigo="1.01.00.00-8"),
        curso_fk=Curso.objects.get(nome="Ensino Médio")
    )
    disciplina1.nome = "Matemática 3º Ano"
    # disciplina1.area_conhecimento_fk = AreaConhecimento.objects.get(
    #     codigo="1.01.00.00-8")
    disciplina1.carga_horaria = 80
    disciplina1.save()
    # disciplina1.curso_fk = Curso.objects.get(codigo="ESM-3A")
    # disciplina1.professor_fk = Professor.objects.get(id=1)


def create_diario():
    diario = Diario.objects.create(
        disciplina_fk=Disciplina.objects.get(codigo="MAT-3A"),
        professor_fk=Professor.objects.get(cadastro_fk="SERV-002")
    )

    diario.inicio = datetime.date(2022, 2, 2)
    diario.fim = datetime.date(2024, 2, 2)
    diario.ano_semestre = "2022_1"
    diario.save()


def create_aluno():
    logger.info("Criando dados da tabela 'aluno'...")
    # Cria 15 alunos no banco
    for i in range(0, 16):
        # Cada aluno precisa do seu cadastr0
        alunoCad = Cadastro.objects.create(
            matricula="DISC-00"+str(i),
            idade=17,
        )
        alunoCad.nome = names.get_full_name()
        alunoCad.telefone = "(011)9999999"
        alunoCad.email = alunoCad.nome.split(" ")[0] + "@univesp.br"
        alunoCad.senha = "123"
        alunoCad.save()

        # Dados do Aluno
        aluno = Aluno.objects.create(
            cadastro_fk=alunoCad,
            curso_fk = Curso.objects.get(nome="Ensino Médio")
        )

        aluno.serie = 3
        aluno.save()


def create_diarioalunos():
    logger.info("Criando dados da tabela 'diarioalunos'...")
    diario = Diario.objects.get(disciplina_fk="MAT-3A")
    alunos = Aluno.objects.all()
    for aluno in alunos:
        # diario_alunos = DiarioAlunos.objects.create()
        # diario_alunos.diario_fk.add(diario)
        # diario_alunos.aluno_fk.add(aluno)
        DiarioAlunos.objects.create(
            diario_fk=diario,
            aluno_fk=aluno
        )


def clear_cadastro():
    logger.info("Deletando todos os dados de 'cadastro  '")
    Cadastro.objects.all().delete()


def clear_areaconhecimento():
    logger.info("Deletando todos os dados de 'areaconhecimento'")
    AreaConhecimento.objects.all().delete()


def clear_professor():
    # Deleta todos os dados de "professor"
    logger.info("Deletando todos os dados de 'professor'")
    Professor.objects.all().delete()


def clear_curso():
    # Deleta todos os dados de "curso"
    logger.info("Deletando todos os dados de 'curso'")
    Curso.objects.all().delete()


def clear_disciplina():
    # Deleta todos os dados de "disciplina"
    logger.info("Deletando todos os dados de 'disciplina'")
    Disciplina.objects.all().delete()


def clear_aluno():
    # Deleta todos os dados de "aluno"
    logger.info("Deletando todos os dados de 'aluno'")
    Aluno.objects.all().delete()


def clear_diario():
    # Deleta todos os dados de "aluno"
    logger.info("Deletando todos os dados de 'aluno'")
    Diario.objects.all().delete()


def clear_diarioalunos():
    # Deleta todos os dados de "aluno"
    logger.info("Deletando todos os dados de 'aluno'")
    DiarioAlunos.objects.all().delete()
