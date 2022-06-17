
from django.urls import path, include
from . import professor_views, views, gestor_views

urlpatterns = [
    # URLs para funcionalidades de gestor
    path('', views.login_screen, name="login_screen"),
    path('login/', views.do_login, name="do_login"),
    path('logout/', views.logout, name="logout"),
    
    # URLs para funções de professor
    # TODO: Retirar o id do professor do PATH. Quando ele logar, o id deve ficar armazenada em cookie ou algo do gênero
    path('prof/<int:prof_id>/home/', professor_views.home, name="professor_home"),
    # TODO: Retirar o id do professor do PATH. Quando ele logar, o id deve ficar armazenada em cookie ou algo do gênero
    path('prof/<int:prof_id>/profile/', professor_views.profile, name="professor_profile"),
    # Página que listará todas as disciplinas
    path('prof/<int:prof_id>/disciplinas/', professor_views.disciplinas, name="professor_disciplinas"),
    # Página que listará dados de uma disciplina
    path('prof/<int:prof_id>/disciplinas/<int:disciplina_id>', professor_views.disciplina_select, name="disciplina_selecionada"),
    # Página que listará os alunos de uma disciplina. Será possível alterar as datas
    path('prof/<int:prof_id>/disciplinas/<int:disciplina_id>/alunos', professor_views.disciplina_alunos, name="disciplina_alunos"),
      
    # URLs para funcionalidades de gestor
    path('gestor_home/', gestor_views.home, name="gestor_home"),
]