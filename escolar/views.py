from django.shortcuts import render, redirect

# Create your views here.
def login_screen(request):
    context = {'first_name': 'Johnny'}
    return render(request, 'login.html', context)

def do_login(request):
    return redirect('/prof/SERV-002/home')

def logout(request):
    return redirect('/prof_home')

def pesquisa_notas(request):
    context = {'first_name': 'Johnny'}
    return render(request, 'hello.html', context)