from django.urls import path
from .views import *

urlpatterns = [
    path('category/<int:category_id>/', get_category, name='category'),
    path('news/<int:news_id>/', view_news, name='view-news'),
    path('news/add_news/', add_news, name='add-news'),
    path('', index, name='home'),
]
