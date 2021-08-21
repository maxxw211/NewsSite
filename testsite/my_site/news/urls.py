from django.urls import path
from .views import *

urlpatterns = [
    path('category/<int:category_id>/', GetCategory.as_view(), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view-news'),
    path('news/add_news/', AddNews.as_view(), name='add-news'),
    path('', HomeNewsPage.as_view(), name='home'),
]
