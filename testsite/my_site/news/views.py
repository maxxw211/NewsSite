from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Category
from .forms import NewsForm
from django.views.generic import ListView, DetailView, CreateView


class HomeNewsPage(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


# def index(request):
# published_news = list()
#    news = News.objects.filter(is_published=True)
# for new in range(len(news)):
#    if news[new].is_published:
#        published_news.extend({news[new]})
#    context = {'news': news, 'title': 'Список новостей'}
#    return render(request, template_name='news/index.html', context=context)

class GetCategory(ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GetCategory, self).get_context_data(**kwargs)
        context['category_title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


# def get_category(request, category_id):
# published_news = list()
#    news = News.objects.filter(category_id=category_id, is_published=True)
# for new in range(len(news)):
#    if news[new].is_published:
#       published_news.extend({news[new]})
#    category = Category.objects.get(pk=category_id)
#    context = {'news': news, 'category': category}
#    return render(request, template_name='news/category.html', context=context)


class ViewNews(DetailView):
    model = News
    # pk_url_kwarg = 'news_id'
    template_name = 'news/view_news.html'
    context_object_name = 'news_item'


# def view_news(request, news_id):
#    # news_item = News.objects.get(pk=news_id)
#    news_item = get_object_or_404(News, pk=news_id)
#    context = {'news_item': news_item}
#    return render(request, template_name='news/view_news.html', context=context)


class AddNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'

# def add_news(request):
#    if request.method == 'POST':
#        form = NewsForm(request.POST, request.FILES)
#        if form.is_valid():
#            # news_form = News.objects.create(**form.cleaned_data)
#            news_form = form.save()
#           return redirect(news_form)
#        else:
#           form = NewsForm()
#    context = {'form': form}
#    return render(request, 'news/add_news.html', context=context)
