from django.urls import path

from . import views

appname = 'searchbooks'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('search_page', views.search_page, name='search'),
    path('search_results', views.search_results, name='search_results')
]
