from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
)


urlpatterns = [  # needed url links, as specified in the specs
    path(
        'articles',
        ArticleListView.as_view(),
        name='articles'
    ),
    path(
        'article/<int:pk>',
        ArticleDetailView.as_view(),
        name='article_detail'
    ),
    path(
        'article/add',
        ArticleCreateView.as_view(),
        name="article_create"
    ),
    path(
        'article/<int:pk>/edit',
        ArticleUpdateView.as_view(),
        name="article_update"
    ),
]

app_name = 'wiki'
