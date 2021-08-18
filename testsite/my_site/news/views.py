from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Category
from .forms import NewsForm


def index(request):
    news = News.objects.all()
    context = {'news': news, 'title': 'Список новостей'}
    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {'news': news, 'category': category}
    return render(request, template_name='news/category.html', context=context)


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    context = {'news_item': news_item}
    return render(request, template_name='news/view_news.html', context=context)


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news_form = News.objects.create(**form.cleaned_data)
            return redirect(news_form)
    else:
        form = NewsForm()
    context = {'form': form}
    return render(request, 'news/add_news.html', context=context)
