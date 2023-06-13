import time
from django.db import models
from django.shortcuts import render
from education.models import *
from rest_framework.views import APIView
from django.db.models import Q
from django.db import models as dmodels
from education.models import UniversityModel ,CourseModel,AboutModel,FeedModel
from .serializer import *
from rest_framework import status
from rest_framework.response import Response
from .serializer import UniversitySerializer,CourseSerializer,AboutSerializer,FeedSerializer,NotificationSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
# Create your views here.


# University List


class UniversityListView(APIView):
#     permission_classes =[IsAuthenticated]

    def get(self, request, *args, **kwargs):
     try:
        objects = UniversityModel.objects.filter(is_deleted=False)
        serializer = UniversitySerializer(objects, many=True)
      
        res_data = {
            'success': True,
            "message": 'Successfully listed all university',
            'data': serializer.data
        }
        return Response(res_data, status=status.HTTP_200_OK)
     except Exception as ex:
        res_data = {
            'success': False,
            "message": 'Something went wrong',
            'data': str(ex)
            }
        return Response(res_data, status=status.HTTP_400_BAD_REQUEST)

    
class CourseListView(APIView):
    permission_classes =[IsAuthenticated]


    def get(self, request, *args, **kwargs):
     try:
        objects = CourseModel.objects.filter(is_deleted=False)
        serializer = CourseSerializer(objects, many=True)
      
        res_data = {
            'success': True,
            "message": 'Successfully listed all course',
            'data': serializer.data
        }
        return Response(res_data, status=status.HTTP_200_OK)
     except Exception as ex:
        res_data = {
            'success': False,
            "message": 'Something went wrong',
            'data': str(ex)
            }
        return Response(res_data, status=status.HTTP_400_BAD_REQUEST)


#UNIVERSITY VIEW

class CourseDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            obj = CourseModel.objects.get(id=id)
            return obj
        except obj.DoesNotExist:
            return None

    def get(self, request, id):
        try:
            object = self.get_object(id)
            serializer = CourseSerializer(object)
            res_data = {
                'success': True,
                "message": 'Successuflly Fetched',
                'data': serializer.data
            }
            return Response(res_data, status=status.HTTP_200_OK)
        except Exception as ex:
            res_data = {
                'success': False,
                'message': 'Something went wrong',
                'data': str(ex)
            }
            return Response(res_data, status=status.HTTP_400_BAD_REQUEST)

class UniversityDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            obj = UniversityModel.objects.get(id=id)
            return obj
        except obj.DoesNotExist:
            return None

    def get(self, request, id):
        try:
            object = self.get_object(id)
            serializer = UniversitySerializer(object)
            res_data = {
                'success': True,
                "message": 'Successuflly Fetched',
                'data': serializer.data
            }
            return Response(res_data, status=status.HTTP_200_OK)
        except Exception as ex:
            res_data = {
                'success': False,
                'message': 'Something went wrong',
                'data': str(ex)
            }
            return Response(res_data, status=status.HTTP_400_BAD_REQUEST)


class FeedListView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request, *args, **kwargs):
     try:
        objects = FeedModel.objects.filter(is_deleted=False)
        serializer = FeedSerializer(objects, many=True)
      
        res_data = {
            'success': True,
            "message": 'Successfully listed all feed',
            'data': serializer.data
        }
        return Response(res_data, status=status.HTTP_200_OK)
     except Exception as ex:
        res_data = {
            'success': False,
            "message": 'Something went wrong',
            'data': str(ex)
            }
        return Response(res_data, status=status.HTTP_400_BAD_REQUEST)

class AboutListView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request, *args, **kwargs):
     try:
        objects = AboutModel.objects.filter(is_deleted=False)
        serializer = AboutSerializer(objects, many=True)
      
        res_data = {
            'success': True,
            "message": 'Successfully listed all about',
            "message": 'Successfully listed all About',
            'data': serializer.data
        }
        return Response(res_data, status=status.HTTP_200_OK)
     except Exception as ex:
        res_data = {
            'success': False,
            "message": 'Something went wrong',
            'data': str(ex)
            }
        return Response(res_data, status=status.HTTP_400_BAD_REQUEST)

class MCQInitialListView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request, *args, **kwargs):
     try:
        objects = MCQInitialModel.objects.filter(is_deleted=False)
        serializer = MCQInitialSerializer(objects, many=True)
      
        res_data = {
            'success': True,
            "message": 'Successfully listed all mcq initial',
            'data': serializer.data
        }
        return Response(res_data, status=status.HTTP_200_OK)
     except Exception as ex:
        res_data = {
            'success': False,
            "message": 'Something went wrong',
            'data': str(ex)
            }
        return Response(res_data, status=status.HTTP_400_BAD_REQUEST)

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request, *args, **kwargs):
     try:
        objects = NotificationModel.objects.filter(is_deleted=False)
        serializer = NotificationSerializer(objects, many=True)
      
        res_data = {
            'success': True,
            "message": 'Successfully listed all notification',
            'data': serializer.data
        }
        return Response(res_data, status=status.HTTP_200_OK)
     except Exception as ex:
        res_data = {
            'success': False,
            "message": 'Something went wrong',
            'data': str(ex)
            }
        return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
class NotificationOfferListView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request, *args, **kwargs):
     try:
        objects = NotificationModel.objects.filter(is_deleted=False,is_offer=True)
        serializer = NotificationSerializer(objects, many=True)
      
        res_data = {
            'success': True,
            "message": 'Successfully listed all notification',
            'data': serializer.data
        }
        return Response(res_data, status=status.HTTP_200_OK)
     except Exception as ex:
        res_data = {
            'success': False,
            "message": 'Something went wrong',
            'data': str(ex)
            }
        return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
class SlotListView(APIView):
    permission_classes = [IsAuthenticated]

   
    def get(self, request,*args, **kwargs,):
     try:
        objects = SlotModel.objects.filter(is_deleted=False)
        serializer = SlotSerializer(objects, many=True)
      
        res_data = {
            'success': True,
            "message": 'Successfully listed all slot',
            'data': serializer.data
        }
        return Response(res_data, status=status.HTTP_200_OK)
     except Exception as ex:
        res_data = {
            'success': False,
            "message": 'Something went wrong',
            'data': str(ex)
            }
        return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
class SlotIdView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            obj = SlotModel.objects.get(id=id)
            return obj
        except obj.DoesNotExist:
            return None

    def get(self, request, id):
        try:
            object = self.get_object(id)
            serializer = SlotSerializer(object)
            res_data = {
                'success': True,
                "message": 'Successuflly Fetched',
                'data': serializer.data
            }
            return Response(res_data, status=status.HTTP_200_OK)
        except Exception as ex:
            res_data = {
                'success': False,
                'message': 'Something went wrong',
                'data': str(ex)
            }
            return Response(res_data, status=status.HTTP_400_BAD_REQUEST)

        
class TeachContentListView(APIView):
    # permission_classes = [IsGetOrIsAdmin]

    def get(self,request):
        try:
            category = request.GET.get('category')
            subcategory = request.GET.get('subcategory')
            if category is not None:
                categories = Categories.objects.filter(is_active=True,is_deleted=False,main_catogory=category).order_by("id")
            else:
                categories = Categories.objects.filter(is_active=True,is_deleted=False).order_by("id")

            if subcategory is not None:
                objects = TeachContentModel.objects.filter(is_active=True,is_deleted=False,catogory=subcategory).order_by("id")
                serializer = TeachContentSerializer(objects, many=True)
            else:
                serializer = CategoriesSerializer(categories, many=True)
            filters = dmodels.Q()
            # object = TeachContentModel.objects.filter(is_deleted=False)
            # serializer = TeachContentSerializer(object, many=True)
            res_data = {
                'success': True,
                "message": 'Successfully listed content',
                'data': serializer.data
                
            }
            
            return Response(res_data, status=status.HTTP_200_OK)
        except Exception as ex:
            res_data = {
                'success': False,
                "message": 'Something went wrong',
                'data': str(ex)
                }
            return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
        
class bookmark(APIView):
     
    
    
    def post(self, request, *args, **kwargs):
        user_obj =request.user
        post_data = request.data
        post_data.update({'user':user_obj.id})
        # obj_t = LikeButtonModel.objects.all()      
        serializer = bookmarkSerializer(data=post_data)
        print(serializer)
        if serializer.is_valid():
            obj = serializer.save()
            obj.created_by = request.user
            # obj.from_user = from_user
            obj.save()
            res_data = {
                'success': True,
                "message": 'Successfully Created',
                'data': serializer.data
            }
            return Response(res_data, status=status.HTTP_201_CREATED)
        
        else:
            user_id = request.user.id
            print(user_id)
            bookmark_idd = post_data['obj_id']
            bookmark = BookMarks.objects.get(user=user_id,obj_id=bookmark_idd)
            dislike = bookmark.book_mark
            print(dislike)


            if dislike == True:
                bookmark.book_mark = False
                bookmark.save()
                res_data = {
                    'success': True,
                    "message": 'Like change to dislike',
                    'data': None
                }
                return Response(res_data, status=status.HTTP_200_OK)
            

            elif dislike == False:
                bookmark.book_mark = True
                print(bookmark.book_mark)
                bookmark.save()
                res_data = {
                    'success': True,
                    "message": 'Dislike change to like',
                    'data': None
                }
                return Response(res_data, status=status.HTTP_200_OK)
            

            else:

                res_data = {
                    'success': False,
                    "message": 'Listing Creation Failed',
                    'data': serializer.errors
                }
                return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
         
class BookmarkDetailsByIDView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            user_ob =request.user.id
            objects = BookMarks.objects.filter(book_mark=True,user=user_ob)
            serializer = bookmarkSerializer(objects, many=True)
        
            res_data = {
                'success': True,
                "message": 'Successfully listed all feed',
                'data': serializer.data
            }
            return Response(res_data, status=status.HTTP_200_OK)
        except Exception as ex:
            res_data = {
                'success': False,
                "message": 'Something went wrong',
                'data': str(ex)
                }
            return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
    # permission_classes = [IsGetOrIsAuthenticated]
    # parser_classes = (MultiPartParser, FormParser)

class GalaryView(APIView):
    def get(self, request,id,*args, **kwargs):
        try:
            

            objects = galary.objects.filter(univesity_id=id)
           
            serializer = GalarySerializer(objects, many=True)
         
            
            res_data = {
                'success': True,
                "message": 'Successfully listed all notification',
                'data': serializer.data
            }
            return Response(res_data, status=status.HTTP_200_OK)
        except Exception as ex:
            res_data = {
                'success': False,
                "message": 'Something went wrong',
                'data': str(ex)
                }
        return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
    



class paymentSlipCreateView(APIView):
    # permission_classes = [IsAuthenticated]
        
    def post(self, request, *args, **kwargs):
        user_obj =request.user
        
        post_data = request.data
        post_data.update({'user':user_obj.id})
        # obj_t = paymentSerializer.objects.all()      
        serializer = paymentSerializer(data=post_data)
        
        if serializer.is_valid():
            
            obj = serializer.save()
            obj.created_by = request.user
            # obj.from_user = from_user
            obj.save()
            res_data = {
                'success': True,
                "message": 'Successfully Created',
                'data': serializer.data
            }
            return Response(res_data, status=status.HTTP_201_CREATED)
        
        else:
           

            res_data = {
                'success': False,
                "message": 'Listing Creation Failed',
                'data': serializer.errors
            }
            return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
        

class applicationCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self,user_id,id):
            try:
                obj = ApplicationModel.objects.get(created_by=user_id,course=id)
                return obj
            except obj.DoesNotExist:
                return None
        
    def post(self, request, *args, **kwargs):
        print("user :", request.user)
        id = request.user.id
        post_data = request.data
        post_data.update({'user':id})
        serializer = applicationSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            obj.created_by = request.user
            obj.save()
            res_data = {
                'success': True,
                "message": 'Successfully Created',
                'data': serializer.data
            }
            return Response(res_data, status=status.HTTP_201_CREATED)
        else:
            res_data = {
                'success': True,
                "message": 'Program Creation Failed',
                'data': serializer.errors
            }
            return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
        
    
    def put(self, request,id,*args, **kwargs):
        try:
            user_id = request.user
            post_data = request.data
            post_data.update({'user':user_id.id})
            object = self.get_object(user_id,id)
            if object is not None:
                serializer = applicationSerializer(object, data=request.data)

                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    res_data = {
                        'success': True,
                        "message": "Successfully Updated",
                        'data': serializer.data
                    }
                    return Response(res_data, status=status.HTTP_202_ACCEPTED)
                else:
                    res_data = {
                        'success': False,
                        "message": "Department Updation failed",
                        'data': str(ex)
                    }
                    return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
            else:
                res_data = {
                        'success': False,
                        "message": " Updation failed",
                        'data': str(ex)
                    }
                return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as ex:
            res_data = {
                'success': False,
                'message': 'Something went wrong',
                'data': str(ex)
            }
            return Response(res_data, status=status.HTTP_400_BAD_REQUEST) 
        
    def get(self, request,*args, **kwargs):
        try:  
            user_id = request.user.id
            objects = ApplicationModel.objects.filter(created_by=user_id)     
            serializer = applicationSerializer(objects, many=True)       
            res_data = {
                'success': True,
                "message": 'Successfully listed all notification',
                'data': serializer.data
            }
            return Response(res_data, status=status.HTTP_200_OK)
        except Exception as ex:
            res_data = {
                'success': False,
                "message": 'Something went wrong',
                'data': str(ex)
                }
        return Response(res_data, status=status.HTTP_400_BAD_REQUEST)       

# class applicationDetailedView(APIView):
   

   
    


# class shortListView(APIView):
#     # permission_classes = [IsGetOrIsAdmin]

#     def get(self,request):
#         try:
#             country = request.GET.get('country')
#             subcategory = request.GET.get('subcategory')
#             if country is not None:
#                 country = UniversityModel.objects.filter(is_active=True,is_deleted=False,main_catogory=country).order_by("id")
#             else:
#                 country = UniversityModel.objects.filter(is_active=True,is_deleted=False).order_by("id")

#             if subcategory is not None:
#                 objects = UniversityModel.objects.filter(is_active=True,is_deleted=False,country=subcategory).order_by("id")
#                 serializer = UniversitySerializer(objects, many=True)
#             else:
#                 serializer = UniversitySerializer(country, many=True)
#             filters = dmodels.Q()
#             # object = TeachContentModel.objects.filter(is_deleted=False)
#             # serializer = TeachContentSerializer(object, many=True)
#             res_data = {
#                 'success': True,
#                 "message": 'Successfully listed content',
#                 'data': serializer.data
                
#             }
            
#             return Response(res_data, status=status.HTTP_200_OK)
#         except Exception as ex:
#             res_data = {
#                 'success': False,
#                 "message": 'Something went wrong',
#                 'data': str(ex)
#                 }
#             return Response(res_data, status=status.HTTP_400_BAD_REQUEST)

class ApplicationSubmitCreateView(APIView):
    permission_classes = [IsAuthenticated]
        
    def post(self, request, *args, **kwargs):
        user_obj =request.user
        post_data = request.data
        post_data.update({'user':user_obj.id})
        obj_t = ApplicationSubmit.objects.all()      
        serializer = applicationSubmitSerializer(data=post_data)
        if serializer.is_valid():
            obj = serializer.save()
            obj.created_by = request.user
            # obj.from_user = from_user
            obj.save()
            res_data = {
                'success': True,
                "message": 'Successfully Created',
                'data': serializer.data
            }
            return Response(res_data, status=status.HTTP_201_CREATED)       
        else:
           

            res_data = {
                'success': False,
                "message": 'Application already existing',
                'data': None
            }
            return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
