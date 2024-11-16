from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('favourites/', include('favourites.urls', namespace='favourites')),
    path('login/', include('login.urls', namespace='login')),
    path('registration/', include('register.urls', namespace='registration')),
    path('books/', include('books.urls', namespace='books')),
    path('', include('homepage.urls', namespace='homepage')),
]
