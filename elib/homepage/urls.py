from django.urls import path
from .views import HomepageListView

app_name = 'homepage'

urlpatterns = [
    path('', HomepageListView.as_view(), name='home'),
]
