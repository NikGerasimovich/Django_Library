from django.urls import include, re_path
from . import views

urlpatterns = [

    re_path(r'^$', views.index, name='index'),
    re_path(r'^books/$', views.BookListViews.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailViews.as_view(), name='book-detail'),
    re_path(r'authors/$', views.AuthorListViews.as_view(), name='author'),
    re_path(r'author//(?P<pk>\d+)$', views.AuthorDetailViews.as_view(), name='author-detail'),

]
