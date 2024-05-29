from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('authenticate/token/', TokenObtainPairView.as_view(), name='Token-Obtain-Pair'),
    path('authenticate/token/refresh/', TokenRefreshView.as_view(), name='Token-Refresh-Pair'),
    path('authenticate/token/verify/', TokenVerifyView.as_view(), name='Token-Verify-Pair'),
]