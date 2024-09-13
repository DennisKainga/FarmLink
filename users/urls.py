from django.urls import path
from .views import RegisterView
app_name = 'users'
urlpatterns = [
    path('registration/', RegisterView.as_view(), name='registration'),
]
