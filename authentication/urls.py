# blog/urls.py
from django.urls import include, path
from .views import *
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, )

app_name = 'authentications'

urlpatterns = [
    path('', index, name="index"),
    path('register', RegisterAPI.as_view(), name='register'),
    path('login', UserLoginView.as_view(), name='login'),
    path('home', HomePageAPIView.as_view(), name='home'),
    path('add_question', AddQuestionAPIView.as_view(), name='add-question-api'),
    path('add_notification', AddNotificationAPIView.as_view(), name='add-notification-api'),
    path('user/search', SearchApi.as_view(), name='search'),
    path('logout', LogoutView.as_view(), name='auth_logout'),
    path('mood', MoodView.as_view(), name='mood'),
    path('user/',UserProfileUpdate.as_view(), name='user_update'),
    path('user_list',UserProfileUpdate.as_view(), name='user_listing'),
    # path('mood/<int:id>', MoodView.as_view(), name='mood'),
    path('send-otp', PreLoginView.as_view(), name='send-otp'),
    # path('logout-all', LogoutAllView.as_view(), name='auth_logout_all'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('change_password/<int:pk>', ChangePasswordView.as_view(), name='auth_change_password'),
    path('password_reset', include('django_rest_passwordreset.urls', namespace='password_reset')),
    # path('password_reset/confirm', reset_password_confirm, name='password_reset_confirm'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]