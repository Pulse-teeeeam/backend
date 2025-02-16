from . import views
from django.urls import path, include

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('ELC/', views.ELCLogin.as_view(), name='ELC-webhook'),
    path('ELC/generate', views.ELCGenerate.as_view(), name='ELC-webhook'),
]