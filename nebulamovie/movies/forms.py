from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','score',]

class PostFormwithmovie(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['movie', 'title','content','score', ]
        
        
class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['score','content',]
        
        
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['genres', 'title', 'audience', 'runtime', 'grade', 'popularity', 'release_date', 'vote', 'actor1', 'actor2', 'actor3', 'overview', 'poster_url', 'director',]