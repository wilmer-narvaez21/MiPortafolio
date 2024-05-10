from django.urls import path
from .views import render_posts, post_detail

# url que se identifican con un nombre esto lo podemos hacer con django con esta variable
app_name = 'miblog'

urlpatterns = [
    path('', render_posts, name="posts"),
    path('/<int:post_id>', post_detail, name="post_detail"),
]
