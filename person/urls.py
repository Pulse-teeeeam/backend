from . import views
from django.urls import path, include

urlpatterns = [
    path('get/<int:pk>/', views.GetPerson.as_view(), name='get-person'),
    path('create/', views.CreatePerson.as_view(), name='create-person'),
]