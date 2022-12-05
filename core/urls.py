from django.urls import path
from .views import index, contact, detail, category, author, dates, register, newsletter


urlpatterns = [
    path('',index, name="index"),
    path('contact/',contact, name="contact"),
    path('detail/<int:post_id>',detail, name="detail"),
    path('category/<int:category_id>',category, name="category"),
    path('author/<int:author_id>',author, name="author"),
    path('dates/<int:month_id>/<int:year_id>',dates, name="dates"),
    path('register/',register, name="register"),
    path('newsletter/',newsletter, name="newsletter"),
]