from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic.edit import CreateView

from users.forms import CustomUserCreationForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('favourites/', include('favourites.urls', namespace='favourites')),
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=CustomUserCreationForm,
            success_url=reverse_lazy('homepage:home'),
        ),
        name='registration',
    ),
    path('books/', include('books.urls', namespace='books')),
    path('', include('homepage.urls', namespace='homepage')),
]
