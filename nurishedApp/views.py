# nurishedApp/views.py
# nurishedApp/views.py
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import UpdateView
from django.db.models import Count
from django.utils.text import slugify
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Recipe, Comment
from .forms import CommentForm, RecipeForm

class HomePage(View):
#class index(View):
    def get(self, request):
        recipes = Recipe.objects.order_by('-published_on')[:4]
        liked_recipes = Recipe.objects.annotate(
            like_count=Count('likes')).order_by('-like_count')[:5]
        context = {
            "recipes": recipes,
            "liked_recipes": liked_recipes,
        }
        return render(request, 'index.html', context)

class SearchRecipe(View):
    def get(self, request):
        return render(request, 'search.html')

    def post(self, request):
        searched = request.POST.get('searched')
        recipes = Recipe.objects.filter(title__icontains=searched)
        paginator = Paginator(recipes, 6)  # Show 6 recipes per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
            'searched': searched
        }
        return render(request, 'search.html', context)

class AllRecipes(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.order_by('-published_on')
    template_name = 'all_recipes.html'
    paginate_by = 6

class RecipeDetails(View):
    def get(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)
        comments = recipe.comments.order_by('created_on')
        liked = False
        if recipe.likes.filter(id=request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_details.html",
            {
                "recipe": recipe,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )

    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)
        comments = recipe.comments.order_by('created_on')
        liked = False
        if recipe.likes.filter(id=request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
            return HttpResponseRedirect(reverse('recipe_details', args=[slug]))
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_details.html",
            {
                "recipe": recipe,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return HttpResponseRedirect(reverse('recipe_details', args=[comment.recipe.slug]))

class RecipeLike(View):
    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)
        return HttpResponseRedirect(reverse('recipe_details', args=[slug]))

class YourRecipes(View):
    def get(self, request):
        if request.user.is_authenticated:
            recipes = Recipe.objects.filter(author=request.user)
            paginator = Paginator(recipes, 6)  # Show 6 recipes per page
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'your_recipes.html', {"page_obj": page_obj})
        else:
            return render(request, 'your_recipes.html')

class FavouriteRecipes(View):
    def get(self, request):
        if request.user.is_authenticated:
            recipes = Recipe.objects.filter(likes=request.user.id)
            paginator = Paginator(recipes, 6)  # Show 6 recipes per page
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'favourite_recipes.html', {"page_obj": page_obj})
        else:
            return render(request, 'favourite_recipes.html')

class AddRecipe(View):
    def get(self, request):
        return render(request, "add_recipe.html", {"recipe_form": RecipeForm()})

    def post(self, request):
        recipe_form = RecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.slug = slugify('-'.join([recipe.title, str(recipe.author)]), allow_unicode=False)
            recipe.save()
            return redirect('your_recipes')
        else:
            messages.error(self.request, 'Please complete all required fields')
            recipe_form = RecipeForm()
        return render(request, "add_recipe.html", {"recipe_form": recipe_form})

def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.delete()
    return redirect(reverse('your_recipes'))