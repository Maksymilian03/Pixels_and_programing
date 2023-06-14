from django.urls import path
from .views import Main_page, ArticleCreateView

urlpatterns = [
    path('', Main_page.as_view(), name='index'),
    path('article/create', ArticleCreateView.as_view(), name='article_crate')
]
