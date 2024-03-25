from django.shortcuts import render

# Create your views here.
def blog(request):

    context = {
        'text':'Olá blog'
    }

    return render(request, 'blog/index.html', context)

def exemplo(request):

    context = {
        'text':'Olá exemplo',
        'title':'Essa é uma página de exemplo - ',
    }

    return render(request, 'blog/exemplo.html', context)
