from django.urls import path, include
from .views import main_page, article_create_form, article_view

urlpatterns = [
    path('', main_page, name='index'),
    path('article', article_create_form, name='create_form'),
    path('article/<int:id>', article_view, name='article_view'),

]
