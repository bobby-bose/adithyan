from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SecondaryEducation,Work,WorkDetails,HigherEducation,Education,Favourites
from .serializers import *
from rest_framework import generics




class ProfileScreenAPIView(APIView):
    def get(self, request, *args, **kwargs):
        secondary_education = SecondaryEducation.objects.all()
        higher_education = HigherEducation.objects.all()
        work = Work.objects.all()
        work_details = WorkDetails.objects.all()
        education = Education.objects.all()
        favourites = Favourites.objects.all()

        secondary_education_serializer = SecondaryEducationSerializer(secondary_education, many=True)
        higher_education_serializer = HigherEducationSerializer(higher_education, many=True)
        work_serializer = WorkSerializer(work, many=True)
        work_details_serializer = WorkDetailsSerializer(work_details, many=True)
        education_serializer = EducationSerializer(education, many=True)
        favourites_serializer = FavouritesSerializer(favourites, many=True)

        response_data = {
            'SecondaryEducation': secondary_education_serializer.data,
            'HigherEducation': higher_education_serializer.data,
            'Work': work_serializer.data,
            'WorkDetails': work_details_serializer.data,
            'Education': education_serializer.data,
            'Favourites': favourites_serializer.data,
        }

        return Response(response_data, status=status.HTTP_200_OK)

class SecondaryEducationCreateView(generics.CreateAPIView):
    queryset = SecondaryEducation.objects.all()
    serializer_class = SecondaryEducationSerializer

class HigherEducationCreateView(generics.CreateAPIView):
    queryset = HigherEducation.objects.all()
    serializer_class = HigherEducationSerializer

class WorkCreateView(generics.CreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

class WorkDetailsCreateView(generics.CreateAPIView):
    queryset = WorkDetails.objects.all()
    serializer_class = WorkDetailsSerializer

class EducationCreateView(generics.CreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class FavouritesCreateView(generics.CreateAPIView):
    queryset = Favourites.objects.all()
    serializer_class = FavouritesSerializer

