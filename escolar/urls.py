
from django.urls import path, include
from . import professor_views, views, gestor_views

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
    # Página que listará todas as disciplinas
    path('prof/<str:prof_matricula>/disciplinas/', professor_views.disciplinas, name="professor-disciplinas"),
    # Página que listará dados de uma disciplina
    path('prof/<int:prof_id>/disciplinas/<int:disciplina_id>', professor_views.disciplina_select, name="disciplina-selecionada"),
    # Página que listará os alunos de uma disciplina. Será possível alterar as datas
    path('prof/<int:prof_id>/disciplinas/<int:disciplina_id>/alunos', professor_views.disciplina_alunos, name="disciplina-alunos"),
      
    # URLs para funcionalidades de gestor
    path('gestor_home/', gestor_views.home, name="gestor-home"),
    # Configurar as outras rotas de gestor
]