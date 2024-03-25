from django.shortcuts import render
from blog.data import posts
# importando a json da api, que tranformei em list de dict

# Create your views here.
def blog(request):

    context = {
        'text':'Olá blog',
        'posts': posts
    }

    return render(request, 'blog/index.html', context)

def exemplo(request):

    context = {
        'text':'Olá exemplo',
        'title':'Essa é uma página de exemplo - ',
    }

    return render(request, 'blog/exemplo.html', context)

def post(request, id):
    print('post', id)

    context = {
        'posts': posts
    }

    return render(request, 'blog/index.html', context)


