from django.shortcuts import render, redirect

def home(request):
    context = {'first_name': 'Johnny'}
    return render(request, '/staff_template/base_template.html', context)
