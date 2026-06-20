from django.shortcuts import render

# Create your views here.
def home(request):
    #variaveis  que eu vou enviar para o template
    context ={
        'nome' : 'Guilherme',
        'sobrenome' : 'Martins de Oliveira'
    }


    #O segundo parametro e o  caminho do html
    return render(request, 'home.html', context)

def contato(request):

    return render(request, 'contato.html')

def exibir_produtos(request):

    produtos =[
        'Notebook',
        'Smartphone',
        'Tablet',
        'Smartwatch',
        'Fone de ouvido'
    ]
    context = {
        'produtos': produtos
    }
    return render(request, 'produtos.html', context)