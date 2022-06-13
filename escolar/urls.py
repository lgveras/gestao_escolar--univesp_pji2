
from django.urls import path, include
from . import views, prof_views, gestor_views

urlpatterns = [
    path('', views.login_screen, name="login_screen"),
    path('login/', views.do_login, name="do_login"),
    
    # URLs para funções de professor
    path('prof_home/', prof_views.home, name="prof_home"),
    
    # URLs para funcionalidades de gestor
    path('gestor_home/', gestor_views.home, name="prof_home"),
]