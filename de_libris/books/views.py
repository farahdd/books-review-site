from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Genre, Book, Author, ReviewRating, Quote
from .forms import ReviewForm,QuoteForm

def book_list(request, genre_slug=None):
    genre = None
    genres = Genre.objects.all()
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 5)
    page_number = request.GET.get('page', 1)
    try:
        books = paginator.page(page_number)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    if genre_slug:
        genre = get_object_or_404(Genre, slug=genre_slug)
        books = Book.objects.filter(genre=genre)
    return render(request, 'book/book_list.html', {
        'genre': genre,
        'genres': genres,
        'books': books
    }) 
    
def review_list(request, book_id, book_slug):
    book = get_object_or_404(Book, id=book_id, slug=book_slug)
    reviews_list = ReviewRating.objects.filter(book_id=book_id, active=True)
    
    paginator = Paginator(reviews_list, 4)
    page_number = request.GET.get('page', 1)
    try:
        reviews = paginator.page(page_number)
    except PageNotAnInteger:
        reviews = paginator.page(1)
    except EmptyPage:
        reviews = paginator.page(paginator.num_pages)
    
    return render(request, 'book/reviews_list.html', {
        'book': book, 
        'reviews': reviews, 
    })

def book_detail(request, id, slug):
    book = get_object_or_404(Book, id=id, slug=slug)
    reviews_total = reviews = ReviewRating.objects.filter(book_id=book.id, active=True)
    reviews = ReviewRating.objects.filter(book_id=book.id, active=True)[0:3]
    quotes = Quote.objects.filter(book_id=book.id)
    
    return render(request, 'book/detail.html', {
        'book': book, 
        'reviews': reviews, 
        'reviews_total': reviews_total,
        'quotes': quotes, 
    })
    
def author_detail(request, id, author_slug):
    author = get_object_or_404(Author, slug=author_slug, id=id)
    books = Book.objects.filter(author_id=id)
    return render(request, 'author_detail.html', {
        'author': author, 'books':books
    })

@login_required   
def create_review(request, id, book_slug):
    book = get_object_or_404(Book, id=id, slug=book_slug)
    review = None
    form = ReviewForm(data=request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.author = request.user
        review.book = book
        review.save()
    return render(request, 'book/review.html', {'review': review, 'form': form, 'book': book})
        
    

@login_required 
def submit_quote(request, id, book_slug):
    book = get_object_or_404(Book, id=id, slug=book_slug)
    quote = None
    form = QuoteForm(data=request.POST)
    if form.is_valid():
        quote = form.save(commit=False)
        quote.author = request.user
        quote.book = book
        quote.save()
    return render(request, 'book/review.html', {'quote': quote, 'form': form, 'book': book})

def home(request):
    genres = Genre.objects.all()
    books = Book.objects.all()
    return render(request, 'index.html', {"genres": genres, 'books': books,})

def genres(request):
    genres = Genre.objects.all()
    return render(request, 'genres_list.html', {
        'genres': genres,
    })
    
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {
        'authors': authors,
    })
    

    
   