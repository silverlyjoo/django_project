from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('follow/<int:user_pk>/', views.follow, name='follow'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('password/', views.change_password, name='change_password'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    ]