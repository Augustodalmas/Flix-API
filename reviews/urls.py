from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.reviewListCreateView.as_view(), name='reviewListCreate'),
    path('reviews/<int:pk>/', views.reviewRetrieveUpdateDeleteView.as_view(), name='reviewDetail'),
]