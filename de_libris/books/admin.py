from django.contrib import admin
from .models import Genre, Book, Author, ReviewRating, Quote

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'slug', 'isbn', 'author', 'published' ]
    list_filter = ['title', 'published']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(ReviewRating)
class ReviewRatingAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'review', 'author', 'book', 'created','rating', 'active']
    list_filter = ['title', 'created', 'author']
    ordering = ['created']
    
@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'quote','created']
    list_filter = ['created', 'author']
    ordering = ['created']