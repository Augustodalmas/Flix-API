from django.urls import path
from . import views

urlpatterns = [
    path('movie/', views.movieCreateListView.as_view(), name='movieListCreate'),
    path('movie/<int:pk>/', views.movieRetrieveUpdateDeleteView.as_view(), name='movieDetail'),
]