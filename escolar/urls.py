from django.urls import path, include
from . import professor_views, views, gestor_views, disciplina_views

urlpatterns = [
    # URLs para funcionalidades de gestor
    path('', views.login_screen, name="login_screen"),
    path('login/', views.do_login, name="do_login"),
    path('logout/', views.logout, name="logout"),
    
    # URLs para funções de professor
    # TODO: Retirar o id do professor do PATH. Quando ele logar, o id deve ficar armazenada em cookie ou algo do gênero
    path('prof/<str:prof_matricula>/home/', professor_views.home, name="professor-home"),
    # TODO: Retirar o id do professor do PATH. Quando ele logar, o id deve ficar armazenada em cookie ou algo do gênero
    path('prof/<str:prof_matricula>/profile/', professor_views.profile, name="professor-profile"),
     # Página que listará dados de uma disciplina
    path('prof/<str:prof_matricula>/disciplinas/', disciplina_views.lista_disciplina, name="lista-disciplinas"),
       
    path('prof/<str:prof_matricula>/disciplinas/<str:disciplina_id>/dados', disciplina_views.dados, name="disciplinas-dados"),
    path('prof/<str:prof_matricula>/disciplinas/<str:disciplina_id>/alunos', disciplina_views.alunos, name="disciplinas-alunos"),
    path('prof/<str:prof_matricula>/disciplinas/<str:disciplina_id>/aulas', disciplina_views.aulas, name="disciplinas-aulas"),
    
    # path('prof/<str:prof_matricula>/disciplinas/<str:disciplina_id>/aulas/add', disciplina_views.add_aula, name="adiciona-aula"),
    

    # URLs para funcionalidades de gestor
    path('gestor_home/', gestor_views.home, name="gestor-home"),
    # Configurar as outras rotas de gestor
]