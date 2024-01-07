# blog/urls.py
from django.urls import include, path
from .views import *
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, )

app_name = 'University'

urlpatterns = [
    path('home', UniversityScreenAPIView.as_view(), name='University_home'),
    path('about/', AboutCreateView.as_view(), name='about-create'),
    path('feed/', FeedCreateView.as_view(), name='feed-create'),
    path('gallery/', GalleryCreateView.as_view(), name='gallery-create'),
    path('courses/', CoursesCreateView.as_view(), name='courses-create'),
]
