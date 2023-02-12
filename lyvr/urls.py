from django.urls import path
from .views import books_example, common, auth
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from library import views
from django.contrib.auth.views import LoginView,LogoutView

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

    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls') ),
    path('', views.home_view),

    path('adminclick', views.adminclick_view),
    path('studentclick', views.studentclick_view),


    path('adminsignup', views.adminsignup_view),
    path('studentsignup', views.studentsignup_view),
    path('adminlogin', LoginView.as_view(template_name='library/adminlogin.html')),
    path('studentlogin', LoginView.as_view(template_name='library/studentlogin.html')),

    path('logout', LogoutView.as_view(template_name='library/index.html')),
    path('afterlogin', views.afterlogin_view),

    path('addbook', views.addbook_view),
    path('viewbook', views.viewbook_view),
    path('issuebook', views.issuebook_view),
    path('viewissuedbook', views.viewissuedbook_view),
    path('viewstudent', views.viewstudent_view),
    path('viewissuedbookbystudent', views.viewissuedbookbystudent),

    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),

]
