# forms.py

from django import forms

# Static options for ratings and release year
RATING_CHOICES = [(i, str(i)) for i in range(1, 11)]  # Rating from 1 to 10
RELEASE_YEAR_CHOICES = [(year, str(year)) for year in range(1900, 2025)]  # Years from 1900 to 2025

class RecommendationForm(forms.Form):
    rating = forms.ChoiceField(choices=RATING_CHOICES, required=False, label='Rating')
    
    # You can statically define genres or dynamically fetch them from the TMDB API
    GENRE_CHOICES = [
        ('28', 'Action'),
        ('12', 'Adventure'),
        ('16', 'Animation'),
        ('35', 'Comedy'),
        ('80', 'Crime'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('science_fiction', 'Science Fiction'),
        ('fantasy', 'Fantasy'),
        # Add more genres as needed...
    ]
    
    genre = forms.ChoiceField(choices=GENRE_CHOICES, required=False, label='Genre')
    
    release_year = forms.ChoiceField(choices=RELEASE_YEAR_CHOICES, required=False, label='Release Year')
    
    # Actor field allows user input
    actor = forms.CharField(max_length=100, required=False, label='Actor')
