from django.shortcuts import render
from django.views import generic
from .models import Article, Author

def home_page(request):
    # Генерация "количеств" некоторых главных объектов
    num_articles = Article.objects.all().count()
    # Доступные книги (статус = 'a')
    num_authors = Author.objects.all().count()  # Метод 'all()' применён по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'home_page.html',
        context={'num_articles': num_articles, 'num_authors': num_authors},
    )

def articles_list(request):
    obj = Article.objects.all()

    return render(
        request,
        'articles_list.html',
        context={'articles_list': obj},
    )

class ArticleDetailView(generic.DetailView):
    template_name = 'articles_detail.html'
    model = Article

def authors_list(request):
    obj = Author.objects.all()

    return render(
        request,
        'authors_list.html',
        context={'authors_list': obj}
    )

class AuthorDetailView(generic.DetailView):
    template_name = 'authors_detail.html'
    model = Author
