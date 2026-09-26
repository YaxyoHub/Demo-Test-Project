from django.urls import path
from .views import (
    home_view, 
    login_view, 
    logout_view, 
    register_view,
    verify_email_view
)

from books.views import books_view
from blog.views import (
    my_posts_view, 
    create_post_view, 
    edit_post_view, 
    delete_post_view,
    send_email_view
)
urlpatterns = [
    path('', home_view, name='home'),

    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),

    path('books/', books_view, name='books'),

    path('send-email/', send_email_view, name='send_email'),
    path('verify-email/', verify_email_view, name='verify_email'),


    path('my-posts/', my_posts_view, name='my_posts'),
    path('create-post/', create_post_view, name='create_post'),
    path('edit-post/<int:pk>', edit_post_view, name='edit_post'),
    path('delete-post/<int:pk>', delete_post_view, name='delete_post'),
]