from django.urls import path
from django.urls import path
from blog.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('post/<int:post_id>/', view_post, name='post'),
    path('category/<int:cat_id>/', view_category, name='category'),
]