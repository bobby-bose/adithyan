from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import About, Feed, Courses, Gallery
from .serializers import AboutSerializer, FeedSerializer, CoursesSerializer, GallerySerializer
from rest_framework import generics


class UniversityScreenAPIView(APIView):
    def get(self, request, *args, **kwargs):
        about_data = About.objects.all()
        feed_data = Feed.objects.all()
        courses_data = Courses.objects.all()
        gallery_data = Gallery.objects.all()

        about_serializer = AboutSerializer(about_data, many=True)
        feed_serializer = FeedSerializer(feed_data, many=True)
        courses_serializer = CoursesSerializer(courses_data, many=True)
        gallery_serializer = GallerySerializer(gallery_data, many=True)

        response_data = {
            'about': about_serializer.data,
            'feed': feed_serializer.data,
            'courses': courses_serializer.data,
            'gallery': gallery_serializer.data,
        }

        return Response(response_data, status=status.HTTP_200_OK)


class AboutCreateView(generics.CreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class FeedCreateView(generics.CreateAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

class GalleryCreateView(generics.CreateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

class CoursesCreateView(generics.CreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer