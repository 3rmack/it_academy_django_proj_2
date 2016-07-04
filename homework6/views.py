#coding: UTF-8
from django.shortcuts import render, redirect
from forms import ArticleForm, SectionForm
from models import Articles, Sections, Connections
from django.http import HttpResponse


def index(request):
    return render(request, 'homework6_index.html')


def view_articles(request):
    articles = Articles.objects.filter()
    context = {'articles': articles}
    return render(request, 'homework6_view_articles.html', context)


def add_article(request):
    if request.method == 'POST':
        raw_data = ArticleForm(request.POST)
        if raw_data.is_valid():
            data = raw_data.cleaned_data
            Articles.objects.create(**data)
            return redirect(view_articles)
        context = {'articles_form': raw_data}
        return render(request, 'homework6_add_article.html', context)
    else:
        articles = Articles.objects.filter()
        context = {'articles_form': ArticleForm(), 'articles': articles}
        return render(request, 'homework6_add_article.html', context)


def view_sections(request):
    sections = Sections.objects.filter()
    context = {'sections': sections}
    return render(request, 'homework6_view_sections.html', context)


def add_section(request):
    if request.method == 'POST':
        raw_data = SectionForm(request.POST)
        if raw_data.is_valid():
            data = raw_data.cleaned_data
            Sections.objects.create(**data)
            return redirect(view_sections)
        context = {'section_form': raw_data}
        return render(request, 'homework6_add_section.html', context)
    else:
        sections = Sections.objects.filter()
        context = {'section_form': SectionForm(), 'sections': sections}
        return render(request, 'homework6_add_section.html', context)


def view_connections(request):
    connections = Connections.objects.filter()
    context = {'connections': connections}
    return render(request, 'homework6_view_connections.html', context)


def add_connections(request):
    if request.method == 'POST':
        article_id = request.POST.get('article')
        section_id = request.POST.get('section')
        article = Articles.objects.get(id=article_id)
        section = Sections.objects.get(id=section_id)
        Connections.objects.create(article=article, section=section)
        return redirect(view_connections)
    else:
        articles = Articles.objects.filter()
        sections = Sections.objects.filter()
        context = {'sections': sections, 'articles': articles}
        return render(request, 'homework6_add_connections.html', context)
