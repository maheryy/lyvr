from django.urls import path
from .views import books_example, common, auth

urlpatterns = [
    path('', common.home, name='home'),
    path('register/', auth.register, name='register'),
    path('pro/register/', auth.register_pro, name='register-pro'),

    # Remove this test later
    path('test-pro/', common.test_pro_view, name='test-pro'),

    
    
    # Remove this example later
    path('books/', books_example.list, name='book-example-list'),
    path('books/new/', books_example.create, name='book-example-new'),
    path('books/<int:id>/', books_example.detail, name='book-example-detail'),
    path('books/<int:id>/edit/', books_example.edit, name='book-example-edit'),
    path('books/<int:id>/delete/', books_example.delete, name='book-example-delete'),
]
