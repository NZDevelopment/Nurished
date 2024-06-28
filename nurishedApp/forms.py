""" forms for Comment and Recipe """
from django import forms
from .models import Comment, Recipe


class CommentForm(forms.ModelForm):
    """ Comment Form"""
    class Meta:
        """ fields for comment form"""
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields[
            'body'
            ].label = ""


class RecipeForm(forms.ModelForm):
    """ Recipe Form """
    class Meta:
        """ fields for recipe form"""
        model = Recipe
        fields = ('title', 'description', 'ingredients',
                  'preparation_steps', 'image')


    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields[
            'image'
            ].label = "You can upload an image here"