from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def fornecedor(request):
    return render(request, 'fornecedor.html')
