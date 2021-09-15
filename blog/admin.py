from django.contrib import admin
from .models import Article, Author

admin.site.register(Author)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_of_writing')
    list_filter = ('date_of_writing',)

admin.site.register(Article, ArticleAdmin)
