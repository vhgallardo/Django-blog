from django.urls import path
from .views import home, users, posts, categories, tags, rss, add_user, user_profile, signin, signout, lockScreen, add_tag, add_category, add_rss


urlpatterns = [
    path('home',home, name="home"),
    path('users/',users, name="users"),
    path('posts/',posts, name="posts"),
    path('categories/',categories, name="categories"),
    path('add_category/',add_category, name="add_category"),
    path('tags/',tags, name="tags"),
    path('add_tag/',add_tag, name="add_tag"),
    path('rss/',rss, name="rss"),
    path('add_rss/',add_rss, name="add_rss"),
    path('add_user/',add_user, name="add_user"),
    path('user_profile/',user_profile, name="user_profile"),
    path('',signin, name="signin"),
    path('signout/',signout, name="signout"),
    path('lock_screen/<int:user_id>',lockScreen, name="lock_screen"),
]