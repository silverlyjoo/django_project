from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path('<int:movie_id>/posts/new/', views.postcreatewithmovie, name="postcreatewithmovie" ),
    path('<int:movie_id>/scores/<int:score_id>/delete/', views.score_delete, name="score_delete" ),
    path('<int:movie_id>/scores/new/', views.score_create, name="score_create" ),
    path('<int:movie_id>/like/', views.like_movie, name="like_movie" ),
    path('<int:movie_id>/', views.moviedetail, name="moviedetail" ),
    
    path('posts/<int:post_id>/edit/', views.post_update, name="post_update"),
    path('posts/<int:post_id>/delete/', views.post_delete, name="post_delete"),
    path('posts/<int:post_id>/rec/', views.rec_post, name="rec_post"),
    path('posts/<int:post_id>/notrec/', views.not_rec_post, name="not_rec_post"),
    path('posts/<int:post_id>/', views.postdetail, name="postdetail"),
    path('posts/new/', views.postcreate, name="postcreate" ),
    path('posts/', views.postlist, name="postlist"),
    
    path('directors/<int:director_id>/', views.listbydirector, name="listbydirector" ),
    path('directors/', views.directorlist, name="directorlist" ),
    
    path('genres/<int:genre_id>/', views.listbygenre, name="listbygenre" ),
    path('genres/', views.genrelist, name="genrelist" ),
    
    path('popularity/', views.poplist, name="poplist" ),
    path('list/f/', views.listbyfollow, name="listbyfollow" ),
    path('list/a/', views.listbyaudience, name="listbyaudience" ),
    path('list/s/', views.listbys_score, name="listbys_score" ),
    path('list/p/', views.listbyp_score, name="listbyp_score" ),
    path('list/t/', views.listbytitle, name="listbytitle" ),
    
    path('explore/', views.explore, name="explore" ),
    path('', views.index, name="index" ),
    ]
    