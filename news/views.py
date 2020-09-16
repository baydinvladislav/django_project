from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm

def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

def create(request):
    eror = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            eror = 'Форма была неверной'


    form = ArticlesForm()

    data = {
        'form': form,
        'eror': eror
    }

    return render(request, 'news/create.html', data)
