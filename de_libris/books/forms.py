from django import forms
from .models import ReviewRating, Quote

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['title', 'review', 'rating']
        
class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['quote']