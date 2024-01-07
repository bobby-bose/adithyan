# blog/urls.py
from django.urls import include, path
from .views import *
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, )

app_name = 'Profile'

urlpatterns = [
    path('home', ProfileScreenAPIView.as_view(), name='Profile_home'),
    path('secondaryeducationcreate/', SecondaryEducationCreateView.as_view(), name='secondaryeducationcreate'),
    path('highereducationcreate/', HigherEducationCreateView.as_view(), name='highereducationcreate'),
    path('workcreate/', WorkCreateView.as_view(), name='workcreate'),
    path('workdetailscreate/', WorkDetailsCreateView.as_view(), name='workdetailscreate'),
  path('educationcreate/', EducationCreateView.as_view(), name='educationcreate'),
    path('favouritescreate/', FavouritesCreateView.as_view(), name='favouritescreate'),
] 
