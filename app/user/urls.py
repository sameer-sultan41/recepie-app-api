from django.urls import path
from user.views import CreateUserView

app_name = 'user'  # This defines the namespace

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
]