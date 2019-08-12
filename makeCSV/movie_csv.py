import requests, os
import sys


movie_key = os.getenv('MOVIE_KEY')

L = []
L2 = []
L3 = []
L4 = []
L5 = []

with open('movietitle.txt','w') as f:
    for page_num in range(1,16):
        movie_url = f"https://api.themoviedb.org/3/movie/popular?api_key={movie_key}&language=ko-KR&page={page_num}"
        for i in range(20):
            req = requests.get(movie_url).json()['results'][i]['title']
            L.append(str(req))
    f.write(','.join(L)+'\r\n')

with open('moviepop.txt','w') as f:
    for page_num in range(1,16):
        movie_url = f"https://api.themoviedb.org/3/movie/popular?api_key={movie_key}&language=ko-KR&page={page_num}"
        for i in range(20):
            req1 = requests.get(movie_url).json()['results'][i]['popularity']
            L2.append(str(req1))
    f.write(','.join(L2)+'\r\n')

with open('movieoverview.txt','w') as f:
    for page_num in range(1,16):
        movie_url = f"https://api.themoviedb.org/3/movie/popular?api_key={movie_key}&language=ko-KR&page={page_num}"
        for i in range(20):
            req2 = requests.get(movie_url).json()['results'][i]['overview']
            L3.append(str(req2))
    f.write(','.join(L3)+'\r\n')

with open('moviedate.txt','w') as f:
    for page_num in range(1,16):
        movie_url = f"https://api.themoviedb.org/3/movie/popular?api_key={movie_key}&language=ko-KR&page={page_num}"
        for i in range(20):
            req3 = requests.get(movie_url).json()['results'][i]['release_date']
            L4.append(str(req3))
    f.write(','.join(L4)+'\r\n')
    
with open('movievote.txt','w') as f:
    for page_num in range(1,16):
        movie_url = f"https://api.themoviedb.org/3/movie/popular?api_key={movie_key}&language=ko-KR&page={page_num}"
        for i in range(20):
            req4 = requests.get(movie_url).json()['results'][i]['vote_average']
            L5.append(str(req4))
    f.write(','.join(L5)+'\r\n')
    