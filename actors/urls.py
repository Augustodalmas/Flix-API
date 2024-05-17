from django.urls import path
from . import views


urlpatterns = [
    path('actors/', views.actorsCreateListView.as_view(), name='actorsListCreate'),
    path('actors/<int:pk>/', views.actorsRetrieveUpdateDeleteView.as_view(), name='actorsDetail'),
]