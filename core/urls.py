
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('lyvr.urls')),
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]