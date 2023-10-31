from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.home, name='home'),
    path('genres/', views.genres, name='genres'), 
    path('genres/<slug:genre_slug>/', views.book_list,
 name='book_list_by_genre'),
    path('book/<int:id>/<slug:slug>/', views.book_detail,
 name='book_detail'),
    path('author/<int:id>/<slug:author_slug>/', views.author_detail,
 name='author_detail'),
    path('author/', views.author_list, name='author_list'),
    path('book/<int:id>/<slug:book_slug>/create_review/', views.create_review, name='create_review'),
    path('book/<int:book_id>/<slug:book_slug>/reviews', views.review_list, name='review_list'),
    path('book/<int:id>/<slug:book_slug>/create_quote/', views.submit_quote, name='submit_quote'),
]
