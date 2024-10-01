from django.utils import timezone
from django.db import models
import uuid
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)  # Make slug optional


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) 
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Movie(models.Model):
    uu_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genres = models.ManyToManyField(Genre, related_name='movies')  # Updated field
    length = models.PositiveIntegerField(help_text="Length of the movie in minutes")
    image_card = models.ImageField(upload_to='movie_images/')
    image_cover = models.ImageField(upload_to='movie_images/')
    video = models.FileField(upload_to='movie_videos/')
    movie_views = models.IntegerField(default=0)

    movie_rate = models.DecimalField(max_digits=3, decimal_places=1, help_text="Rate out of 10")
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1, help_text="IMDb Rating out of 10")
    movie_director = models.CharField(max_length=255, help_text="Director of the movie")
    movie_cast = models.TextField(help_text="Cast of the movie")
    # Adding an optional YouTube link
    youtube_link = models.URLField(blank=True, null=True, help_text="Optional YouTube link for the movie trailer")


    def __str__(self):
        return self.title


class MovieList(models.Model):
    owner_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    customer_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50, default='customer')

    def __str__(self):
        return self.customer_name
    
# Review model for movies
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')  # Linked to Movie instead of Product
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)]  # Ensure rating is between 1 and 5
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Review by {self.user.username} for {self.movie.title}"