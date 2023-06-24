from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Article
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from .forms import ArticleForm, NewForm
# Create your views here.


def article_create_form(request):
    nowy_form = NewForm()
    if request.method == "POST":
        nowy_form = NewForm(request.POST)
        if nowy_form.is_valid():
            print(nowy_form.cleaned_data)
            Article.objects.create(**nowy_form.cleaned_data)
            nowy_form = NewForm()
        else:
            print(nowy_form.errors)

    context = {"form": nowy_form}

    return render(request, 'form.html', context)


def main_page(request):
    articles = Article.objects.all()

    context = {'articles': articles}

    return render(request, 'main_page.html', context)


def article_view(request, id):
    obj = Article.objects.get(ID=id)
    context = {"object": obj}

    return render(request, "View_article.html", context)

# class ArticleCreateView(PermissionRequiredMixin, CreateView):
#     template_name = 'form.html'
#     form_class = ArticleForm
#     success_url = reverse_lazy('index')
#     permission_required = 'blog.create_article'

