from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.

# admin
# wzl12345

def index(request):
    # return HttpResponse('Hello,World!')

    #测试
    # article = models.Article.objects.get(pk=2)
    articles = models.Article.objects.all()
    return render(request,'blog/index.html',{'articles':articles})# 'articles'是index.html中的字段

def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article})

def edit_page(request,article_id):
    if str(article_id) == '0': # 不转换str，会报错 Article matching query does not exist
        return render(request,'blog/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})

def edit_action(request):
    title = request.POST.get('title','TITLE')
    content = request.POST.get('content','CONTENT')
    article_id = request.POST.get('article_id','0')

    if article_id == '0':
        models.Article.objects.create(title=title,content=content)
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})# 返回主页

    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request,'blog/article_page.html',{'article':article})