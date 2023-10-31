
from django.db import models
from django.urls import reverse
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models import Avg, Count

class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='books/%Y/%m', blank=True)
    
    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name']),]
        verbose_name = 'genre'
        verbose_name_plural = 'genres'
        
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('books:book_list_by_genre', args=[self.slug])
        
class Author(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    bio = models.TextField()
    image = models.ImageField(upload_to='authors/%Y/%m', blank=True)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    
    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'author'
        verbose_name_plural = 'authors'
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('books:author_detail',
        args=[self.id, self.slug])


class Book(models.Model):
    isbn = models.CharField(max_length=200, unique=True)
    genre = models.ForeignKey(Genre, related_name='books', on_delete=models.CASCADE)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='books/%Y/%m', blank=True)
    description = models.TextField(blank=False)
    published = models.DateField()
    
    
    class Meta:
        ordering = ['title']
        indexes = [
        models.Index(fields=['id', 'slug']),
        models.Index(fields=['title']),
        models.Index(fields=['-published']),
        ]
        
    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('books:book_detail',
        args=[self.id, self.slug])
        
    
    def averageReview(self):
        reviews = ReviewRating.objects.filter(book=self, active=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = round(float(reviews['average']), 1)
        return avg
        
class ReviewRating(models.Model):
        book = models.ForeignKey(Book,
                             on_delete=models.CASCADE,
                             related_name='rating_reviews')
        title = models.CharField(max_length=300, blank=True)
        review = models.TextField(blank=True)
        author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='reviews')
        rating = models.FloatField()
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        active = models.BooleanField(default=True)
        
        class Meta:
            ordering = ['created']
            indexes = [
                models.Index(fields=['created']), ]       
        
        def __str__(self):
            return f'Review by {self.author} on {self.book}'
        

class Quote(models.Model):
        book = models.ForeignKey(Book,
                             on_delete=models.CASCADE,
                             related_name='quotes')
        author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='quotes')
        quote = models.TextField()
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        
        class Meta:
            ordering = ['created']
            indexes = [
                models.Index(fields=['created']),]
        
        def __str__(self):
            return self.quote