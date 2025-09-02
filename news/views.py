# news/views.py
from django.shortcuts import render, get_object_or_404
from .models import NewPost

def news_home(request):
    news_list = NewPost.objects.all().order_by('-pub_date')
    return render(request, 'news_home.html', {'news_list': news_list})

def news_detail(request, pk):
    post = get_object_or_404(NewPost, pk=pk)
    return render(request, 'news.html', {'post': post})  # ✅ исправлено!
