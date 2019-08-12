from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import *
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.conf import settings
from accounts.models import *

# Create your views here.

# 무비를 인지로순으로
def poplist(request):
    movies = Movie.objects.all().order_by('-popularity')
    
    context = {
        'movies' : movies
    }
    return render(request, 'movies/list.html', context)

# 장르리스트
def genrelist(request):
    genres = Genre.objects.all()
    context = {
        'indexlist':genres,
    }
    return render(request, 'movies/list.html', context)

# 감독리스트
def directorlist(request):
    director = Director.objects.all()
    context = {
        'indexlist':director,
    }
    return render(request, 'movies/list.html', context)

# 메인페이지
def index(request):
    context = {}
    return render(request, 'movies/index.html', context)

# 무비를 영화제목으로
def listbytitle(request):
    
    movies = Movie.objects.all().order_by('title')
    context = { 'movies':movies}
    return render(request, 'movies/list.html', context)

# 장르에 따른 무비리스트 불러오기
def listbygenre(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    movies = genre.genre_movies.all().order_by('title')
    context = {
        'movies':movies,
        'genre':genre,
    }
    return render(request, 'movies/list.html', context)

# 감독에 따른 무비리스트 불러오기 
def listbydirector(request, director_id):
    
    director = get_object_or_404(Director, id=director_id)
    movies = director.movie_set.all().order_by('title')
    context = {
        'movies':movies,
        'director':director,
    }
    return render(request, 'movies/list.html', context)


def listbys_score(request):
    
    movies = Movie.objects.all().order_by('-s_score')
    context = {
        'movies':movies,
    }
    return render(request, 'movies/list.html', context)
    
def listbyp_score(request):
    
    movies = Movie.objects.all().order_by('-p_score')
    context = {
        'movies':movies,
    }
    return render(request, 'movies/list.html', context)
    
def listbyaudience(request):
    
    movies = Movie.objects.all().order_by('-audience')
    context = {
        'movies':movies,
    }
    return render(request, 'movies/list.html', context)



# 무비 디테일
def moviedetail(request, movie_id):
    
    movie = get_object_or_404(Movie, id=movie_id)
    # genres = movie.genre_
    scores = movie.score_set.all().order_by('-pk')
    scoreform = ScoreForm()
    context = {
        'movie':movie,
        'scoreform':scoreform,
        'scores':scores,
    }
    return render(request, 'movies/detail.html', context)
    
# 포스트 작성
@login_required
def postcreate(request):
    if request.method == 'POST':
        post_form = PostFormwithmovie(request.POST)
        
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            
            
            movie = get_object_or_404(Movie, pk=post.movie.pk)
            posts = movie.post_set.all()
            
            sum_score = 0
            for post in posts:
                sum_score += post.score
                
            
            movie.p_score = sum_score/len(posts)
            movie.save()
            
            
            return redirect('movies:postdetail', post.pk)
    else:
        post_form = PostFormwithmovie()
    context = {
        'form': post_form,
    }
    return render(request, 'movies/form.html', context)
    

# 포스트 작성 (무비 태그)
@login_required
def postcreatewithmovie(request, movie_id):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.movie_id = movie_id
            post.save()
            
            
            movie = get_object_or_404(Movie, pk=movie_id)
            posts = movie.post_set.all()
            
            sum_score = 0
            for post in posts:
                sum_score += post.score
            if len(posts):
                movie.p_score = sum_score/len(posts)
            else:
                movie.p_score = None
            movie.save()
            
            return redirect('movies:postdetail', post.pk)
    else:
        post_form = PostForm()
    context = {
        'form': post_form,
    }
    return render(request, 'movies/form.html', context)
    
    
@login_required
def post_update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    if post.user != request.user:
        return redirect('movies:postdetail', post_id)
    
    if request.method == 'POST':
        post_form = PostFormwithmovie(request.POST, instance=post)
        if post_form.is_valid():
            post = post_form.save()
            movie = get_object_or_404(Movie, pk=post.movie.pk)
            posts = movie.post_set.all()
            sum_score = 0
            for post in posts:
                sum_score += post.score
            if len(posts):
                movie.p_score = sum_score/len(posts)
            else:
                movie.p_score = None
            movie.save()
            return redirect('movies:postdetail', post_id)
    else:
        post_form = PostFormwithmovie(instance=post)
        
    context = {'form': post_form,}
    
    return render(request, 'movies/form.html', context)

@login_required
@require_POST
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.user != request.user:
        return redirect('movies:postdetail', post_id)
    post.delete()
    movie = get_object_or_404(Movie, pk=post.movie.pk)
    posts = movie.post_set.all()
    sum_score = 0
    for post in posts:
        sum_score += post.score
    if len(posts):
        movie.p_score = sum_score/len(posts)
    else:
        movie.p_score = None
    movie.save()
    return redirect('movies:postlist')
    
     
    
# 포스트 리스트
def postlist(request):
    posts = Post.objects.all().order_by('-pk')
    context = {
        'posts': posts
    }
    return render(request, 'movies/postlist.html', context)

# 스코어(댓글) 남기기
@login_required 
@require_POST
def score_create(request, movie_id):
    form = ScoreForm(request.POST)
    if form.is_valid():
        score = form.save(commit=False)
        score.user = request.user
        score.movie_id = movie_id
        score.save()
        
        movie = get_object_or_404(Movie, pk=movie_id)
        scores = movie.score_set.all()
            
        sum_score = 0
        for score in scores:
            sum_score += score.score
        if len(scores):
            movie.s_score = sum_score/len(scores)
        else:
            movie.s_score = None
        movie.save()
        
    return redirect('movies:moviedetail', movie_id)

# 스코어 지우기  
@login_required 
@require_POST
def score_delete(request, movie_id, score_id):
    score = get_object_or_404(Score, pk=score_id)
    if request.user != score.user:
        return redirect('movies:detail', movie_id)
    score.delete()
    movie = get_object_or_404(Movie, pk=movie_id)
    scores = movie.score_set.all()
    sum_score = 0
    for score in scores:
        sum_score += score.score
    if len(scores):
        movie.s_score = sum_score/len(scores)
    else:
        movie.s_score = None
    movie.save()
    
    return redirect('movies:moviedetail', movie_id)

# 포스트 디테일페이지
def postdetail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    
    
    context = {
        'post':post,
    }
    
    return render(request, 'movies/postdetail.html', context)



# 포스트 공감, 비공감
@login_required
def rec_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    user = request.user
    if post.rec_users.filter(pk=user.pk).exists():
        post.rec_users.remove(user)
    else:
        post.rec_users.add(user)
    return redirect('movies:postdetail', post_id)
    
@login_required
def not_rec_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    user = request.user
    if post.not_rec_users.filter(pk=user.pk).exists():
        post.not_rec_users.remove(user)
    else:
        post.not_rec_users.add(user)
    return redirect('movies:postdetail', post_id)


@login_required
def like_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        liked = False
    else:
        movie.like_users.add(user)
        liked = True
    context = {
        'liked': liked,
        'count' : movie.like_users.count()
    }
    return JsonResponse(context)
    


@login_required
def explore(request):
    
    
    people = User.objects.all()
    
    context = {
        'people':people,
    }
    return render(request, 'movies/explore.html', context)

@login_required
def listbyfollow(request):
    user = request.user
    
    me = get_object_or_404(get_user_model(), pk=user.pk)
    context = {
        'people':me,
    }
    return render(request, 'movies/list.html', context)
    