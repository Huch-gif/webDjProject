# news/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import NewPost
from .forms import NewsForm

def news_home(request):
    news_list = NewPost.objects.all().order_by('-pub_date')
    return render(request, 'news_home.html', {'news_list': news_list})

def news_detail(request, pk):
    post = get_object_or_404(NewPost, pk=pk)
    return render(request, 'news.html', {'post': post})

@login_required  # Только для авторизованных
def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user  # Привязываем автора
            news.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsForm()
    return render(request, 'news_create.html', {'form': form})
