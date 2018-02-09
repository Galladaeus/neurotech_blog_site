from django.urls import path

from . import views


app_name = 'BlogPosts'
urlpatterns = [
    path('', views.post_view, name='post_view'),
]
