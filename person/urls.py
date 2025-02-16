from . import views
from django.urls import path, include

urlpatterns = [
    path('get/<int:pk>/', views.GetPerson.as_view(), name='get-person'),
    path('get/<int:pk>/generate', views.GenerateAI.as_view(), name='get-person'),
    path('update/<int:pk>/', views.UpdatePerson.as_view(), name='update-person'),
    path('create/', views.CreatePerson.as_view(), name='create-person'),
    path('armed_conflicts_list/', views.ArmedConflictsList.as_view(), name='armed_conflicts_list'),
    path('medals_list/', views.MedalsList.as_view(), name='medals_list'),
    path('find/', views.FindPerson.as_view(), name='find-person'),
]