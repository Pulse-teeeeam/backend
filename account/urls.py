from . import views
from django.urls import path, include

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
]