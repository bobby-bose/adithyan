# blog/urls.py
from django.urls import include, path
from .views import *


app_name = 'education'

urlpatterns = [
    # path('', IndexView.as_view(), name="index"),
    path('university', UniversityListView.as_view(), name='university'),
    path('course', CourseListView.as_view(), name='course'),
    path('university/details/<int:id>', UniversityDetails.as_view(), name='university-details'),
    path('course/details/<int:id>', CourseDetails.as_view(), name='course-details'),
    path('university/about/', AboutListView.as_view(), name='about'),
    path('university/feed/', FeedListView.as_view(), name='feed'),
    path('slot/', SlotListView.as_view(), name='slot'),
    path('slot/<int:id>', SlotIdView.as_view(), name='slot_update'),
    path('mcqinitial', MCQInitialListView.as_view(), name='mcqinitial'),
    path('notification', NotificationListView.as_view(), name='notification'),
    path('notification/offer', NotificationOfferListView.as_view(), name='notification-offer'),
    path('teachcontent', TeachContentListView.as_view(), name='teach-content'),
    path('bookmark/', bookmark.as_view(), name="bookmark"),
    path('bookmarkview/', BookmarkDetailsByIDView.as_view(), name="bookmark-view"),
    path('galaryview/<int:id>', GalaryView.as_view(), name="galary-view"),
    path('payment/', paymentSlipCreateView.as_view(), name="payment-view"),
    path('application/', applicationCreateView.as_view(), name="application-post"),
    path('application/<int:id>', applicationCreateView.as_view(), name="application-put"),
    path('applicationsubmite/', ApplicationSubmitCreateView.as_view(), name="application-put"),
    # path('shortlist', shortListView.as_view(), name='shortlist'),
    
]