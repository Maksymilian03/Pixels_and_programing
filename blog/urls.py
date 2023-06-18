from django.urls import path, include
from .views import Main_page, article_create_form

urlpatterns = [
    path('', Main_page, name='index'),
    path('article', article_create_form, name='create_form')

]
