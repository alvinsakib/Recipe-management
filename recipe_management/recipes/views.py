# recipes/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe

def list_recipes(request):
    query = request.GET.get('q')
    if query:
        recipes = Recipe.objects.filter(title__icontains=query)
    else:
        recipes = Recipe.objects.all()
    return render(request, 'recipes/list_recipes.html', {'recipes': recipes})

def add_recipe(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')

        errors = {}
        if not title:
            errors['title'] = 'Title is required.'
        elif Recipe.objects.filter(title=title).exists():
            errors['title'] = 'A recipe with this title already exists.'

        if errors:
            return render(request, 'recipes/add_recipe.html', {
                'errors': errors,
                'title': title,
                'ingredients': ingredients,
                'instructions': instructions
            })
        else:
            Recipe.objects.create(title=title, ingredients=ingredients, instructions=instructions)
            return redirect('list_recipes')
    else:
        return render(request, 'recipes/add_recipe.html')

def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')

        errors = {}
        if not title:
            errors['title'] = 'Title is required.'
        elif Recipe.objects.filter(title=title).exclude(pk=pk).exists():
            errors['title'] = 'A recipe with this title already exists.'

        if errors:
            return render(request, 'recipes/edit_recipe.html', {
                'errors': errors,
                'recipe': recipe
            })
        else:
            recipe.title = title
            recipe.ingredients = ingredients
            recipe.instructions = instructions
            recipe.save()
            return redirect('list_recipes')
    else:
        return render(request, 'recipes/edit_recipe.html', {'recipe': recipe})

def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('list_recipes')
    return render(request, 'recipes/delete_recipe.html', {'recipe': recipe})