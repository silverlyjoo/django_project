from django.contrib import admin
from .models import *
# Register your models here.



class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]

class DirectorAdmin(admin.ModelAdmin):
    def get_movies(self, obj):
        return "\n".join([str(p.id) for p in obj.movie_set.all()])
    list_display = ['id', 'name', 'get_movies']


class MovieAdmin(admin.ModelAdmin):
    def get_genres(self, obj):
        return "\n".join([str(p.id) for p in obj.genres.all()])
    
    # list_display = ['title','audience','runtime','grade','popularity','release_date','vote','director_id','actor1', 'actor2', 'actor3','overview','poster_url_low','poster_url', ]
    list_display = ['title', 'poster_url']
    
admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Score)
admin.site.register(Post)