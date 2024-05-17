from django.urls import path
from . import views


urlpatterns = [
    path('genres/', views.genresCreateListView.as_view(), name='genreListCreate'),
    path('genres/<int:pk>/', views.genresRetrieveUpdateDeleteView.as_view(), name='genreDetail'),
]