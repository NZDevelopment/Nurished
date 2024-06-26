from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('all_recipes/', views.AllRecipes.as_view(), name='all_recipes'),
    path('<slug:slug>/', views.RecipeDetails.as_view(), name="recipe_details"),
    path('like/<slug:slug>/', views.RecipeLike.as_view(), name='recipe_like'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('your_recipes/', views.YourRecipes.as_view(), name='your_recipes'),
    path('add_recipe/', views.AddRecipe.as_view(), name='add_recipe'),
    path('delete_recipe/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('favourite_recipes/', views.FavouriteRecipes.as_view(), name='favourite_recipes'),
    path('search/', views.SearchRecipe.as_view(), name='search'),
]