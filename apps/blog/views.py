import json
from django.shortcuts import (
    render,
    get_object_or_404
)
from .models import (
    Article,
)


def blogOverview(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'overview.html', context)


def articleView(request, slug):
    article = get_object_or_404(Article, slug=slug)
    content = json.dumps(article.content)
    context = {
        'article': article,
        'content': content
    }
    return render(request, 'article.html', context)