# NEBULA_PROJECT



#### 프로젝트 목표

the movie api 와 유저들이 입력한 정보를 기반으로 영화를 추천하는 사이트를 제작한다.



#### 팀원 정보

정운지, 박성주



#### Workspace

Django (Back-end, Front-end)



#### 모델

##### movies 모델

> Genre
>
> Director
>
> Movie
>
> Post
>
> Score



##### accounts 모델

> Profile
>
> User



#### view 함수 목록 - 핵심 기능



```python
# 무비를 인지로순으로
def poplist(request):
    
# 장르리스트
def genrelist(request):
    
# 감독리스트
def directorlist(request):
    
# 메인페이지
def index(request):
    
# 영화제목에 따른 영화 리스트
def listbytitle(request):
    
# 장르에 따른 영화리스트
def listbygenre(request, genre_id):
    
# 감독에 따른 영화리스트
def listbydirector(request, director_id):

# 댓글 평점에 따른 영화 리스트
def listbys_score(request):
    
# 리뷰 평점에 따른 영화 리스트
def listbyp_score(request):

# 누적 관객수에 따른 영화 리스트
def listbyaudience(request):
 
# 팔로우한 사람에 따른 영화 리스트
@login_required
def listbyfollow(request):
    
# 무비 디테일
def moviedetail(request, movie_id):
    
# 포스트 작성
@login_required
def postcreate(request):
    
# 리뷰 작성
@login_required
def postcreatewithmovie(request, movie_id):
    
# 리뷰 수정
@login_required
def post_update(request, post_id):

# 리뷰 삭제
@login_required
@require_POST
def post_delete(request, post_id):
    
# 리뷰 리스트
def postlist(request):
    
# 스코어(댓글) 남기기
@login_required 
@require_POST
def score_create(request, movie_id):
    
# 스코어 지우기  
@login_required 
@require_POST
def score_delete(request, movie_id, score_id):
    
# 포스트 디테일페이지
def postdetail(request, post_id):
    
# 포스트 공감, 비공감
@login_required
def rec_post(request, post_id):
    
@login_required
def not_rec_post(request, post_id):
    
# 영화 좋아요
@login_required
def like_movie(request, movie_id):
    
# 유저 목록
@login_required
def explore(request):

```



```python
# 회원가입
def signup(request):
    
# 로그인
def login(request):
    
# 로그아웃
@login_required
def logout(request):
    
# 회원 정보 수정
@login_required
def update(request):
    
# 회원 탈퇴
@login_required
@require_POST
def delete(request):
    
# 비밀번호 변경
@login_required
def change_password(request):
    
# 프로필 보여주기
def people(request, username):
    
# 프로필 수정
@login_required
def profile_update(request):
    
# 팔로우하기
@login_required
def follow(request, user_pk):
```



#### URL 목록

##### from base url (~)

```python
gotoadminpage/ # 관리자 페이지
<str:username>/ # 프로필 페이지
```

##### from movies (~/movies/)

```python
<int:movie_id>/posts/new/ # 새 리뷰 작성 (영화 페이지에서 직접 접근)
<int:movie_id>/scores/<int:score_id>/delete/ # 영화 페이지 댓글 삭제
<int:movie_id>/scores/new/ # 영화 페이지 댓글 생성
<int:movie_id>/like/ # 영화 좋아요
<int:movie_id>/ # 영화 페이지
posts/<int:post_id>/edit/ # 리뷰 수정
posts/<int:post_id>/delete/ # 리뷰 삭제
posts/<int:post_id>/rec/ # 리뷰 추천
posts/<int:post_id>/notrec/ # 리뷰 비추천
posts/<int:post_id>/ # 리뷰 페이지
posts/new/ # 새 리뷰
posts/ # 리뷰 목록
directors/<int:director_id>/ # 감독별 영화 목록
directors/ # 감독 목록
genres/<int:genre_id>/ # 장르별 영화 목록
genres/ # 장르 목록
popularity/ # 인기도 순 영화 정렬
list/f/ # 팔로우 기준 영화 정렬
list/a/ # 누적관객수 기준 영화 정렬
list/s/ # 댓글 평점 기준 영화 정렬
list/p/ # 리뷰 평점 기준 영화 정렬
list/t/ # 제목 기준 영화 정렬
explore/ # 유저 목록
/ # 인덱스 (기본) 페이지
```

##### from accounts (~/accounts/)

```python
follow/<int:user_pk>/ # 유저 팔로우
update/ # 유저 정보 업데이트
delete/ # 회원 탈퇴
password/ # 비밀번호 변경
profile/update/ # 프로필 업데이트
logout/ # 로그아웃
login/ # 로그인
signup/ # 회원가입
```





#### 파일 구조

> ##### 프로젝트 폴더
>
> nebula
>
> ##### 앱 폴더
>
> movies
>
> accounts



##### 파일 구조도

```shell
.
├── accounts
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── admin.cpython-36.pyc
│   │   ├── apps.cpython-36.pyc
│   │   ├── forms.cpython-36.pyc
│   │   ├── models.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── views.cpython-36.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-36.pyc
│   │       ├── 0002_profile.cpython-36.pyc
│   │       └── __init__.cpython-36.pyc
│   ├── models.py
│   ├── templates
│   │   └── accounts
│   │       ├── login.html
│   │       ├── people.html
│   │       ├── profile_update.html
│   │       ├── signup.html
│   │       └── update.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── genreslist_utf.csv
├── manage.py
├── movie_director.csv
├── movie_genre.csv
├── movies
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── admin.cpython-36.pyc
│   │   ├── apps.cpython-36.pyc
│   │   ├── forms.cpython-36.pyc
│   │   ├── models.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── views.cpython-36.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20190514_1333.py
│   │   ├── 0003_post_rec_users.py
│   │   ├── 0004_auto_20190514_1511.py
│   │   ├── 0005_auto_20190515_1004.py
│   │   ├── 0006_auto_20190515_1411.py
│   │   ├── 0007_post_not_rec_users.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-36.pyc
│   │       ├── 0002_auto_20190514_1333.cpython-36.pyc
│   │       ├── 0003_post_rec_users.cpython-36.pyc
│   │       ├── 0004_auto_20190514_1511.cpython-36.pyc
│   │       ├── 0005_auto_20190515_1004.cpython-36.pyc
│   │       ├── 0006_auto_20190515_1411.cpython-36.pyc
│   │       ├── 0007_post_not_rec_users.cpython-36.pyc
│   │       └── __init__.cpython-36.pyc
│   ├── models.py
│   ├── static
│   │   ├── css
│   │   │   ├── aos.css
│   │   │   ├── bootstrap
│   │   │   │   ├── bootstrap-grid.css
│   │   │   │   ├── bootstrap-reboot.css
│   │   │   │   └── bootstrap.css
│   │   │   ├── bootstrap-datepicker.css
│   │   │   ├── bootstrap.min.css
│   │   │   ├── bootstrap.min.css.map
│   │   │   ├── jquery-ui.css
│   │   │   ├── magnific-popup.css
│   │   │   ├── mediaelementplayer.css
│   │   │   ├── owl.carousel.min.css
│   │   │   ├── owl.theme.default.min.css
│   │   │   └── style.css
│   │   ├── js
│   │   │   ├── aos.js
│   │   │   ├── bootstrap-datepicker.min.js
│   │   │   ├── bootstrap.min.js
│   │   │   ├── jquery-3.3.1.min.js
│   │   │   ├── jquery-migrate-3.0.1.min.js
│   │   │   ├── jquery-ui.js
│   │   │   ├── jquery.animateNumber.min.js
│   │   │   ├── jquery.countdown.min.js
│   │   │   ├── jquery.magnific-popup.min.js
│   │   │   ├── jquery.stellar.min.js
│   │   │   ├── jquery.sticky.js
│   │   │   ├── jquery.waypoints.min.js
│   │   │   ├── main.js
│   │   │   ├── mediaelement-and-player.min.js
│   │   │   ├── owl.carousel.min.js
│   │   │   ├── popper.min.js
│   │   │   ├── slick.min.js
│   │   │   └── typed.js
│   │   └── movies
│   │       └── images
│   │           ├── alone.jpg
│   │           ├── bg.jpg
│   │           ├── bow (1).png
│   │           ├── bow.png
│   │           ├── candy.png
│   │           ├── cat.jpg
│   │           ├── header.jpg
│   │           ├── planet.png
│   │           ├── roman.jpg
│   │           ├── saturn.png
│   │           ├── space.jpg
│   │           ├── tv.jpg
│   │           ├── 로맨스.jpg
│   │           ├── 배경.jpg
│   │           ├── 장미1.png
│   │           └── 팝콘.jpg
│   ├── templates
│   │   └── movies
│   │       ├── _catch.html
│   │       ├── _directorlist.html
│   │       ├── _footer.html
│   │       ├── _header.html
│   │       ├── _movielist.html
│   │       ├── _nav.html
│   │       ├── _sidebar.html
│   │       ├── _view.html
│   │       ├── detail.html
│   │       ├── explore.html
│   │       ├── explore_detail.html
│   │       ├── form.html
│   │       ├── index.html
│   │       ├── list.html
│   │       ├── postdetail.html
│   │       └── postlist.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── movies.csv
├── nebula
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── settings.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── wsgi.cpython-36.pyc
│   ├── settings.py
│   ├── templates
│   │   └── base.html
│   ├── urls.py
│   └── wsgi.py
└── requirements.txt
```


