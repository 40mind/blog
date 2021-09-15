from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^articles/$', views.articles_list, name='articles_list'),
    url(r'^articles/(?P<pk>\d+)$', views.ArticleDetailView.as_view(), name='article_detail'),
    url(r'^authors/$', views.authors_list, name='authors_list'),
    url(r'^authors/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author_detail'),
]