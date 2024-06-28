# nurishedApp/models.py
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField

class Recipe(models.Model):
    """
    Recipe model
    """
    title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    published_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    ingredients = models.TextField()
    preparation_steps = models.TextField()
    cooking_time = models.IntegerField()  # Added cooking time
    serving_size = models.IntegerField()  # Added serving size
    image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='liked_recipes', blank=True)

    class Meta:
        ordering = ['-published_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('recipe_details', args=[self.slug])

class Comment(models.Model):
    """
    Comment model
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    def get_absolute_url(self):
        return reverse('recipe_details', args=[self.recipe.slug])

        
