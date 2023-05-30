from django.shortcuts import render
import json
from datetime import datetime, timedelta, timezone
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from .models import BlogModel
from .serializer import *
from django.contrib.auth import get_user_model
from .common.permissions import IsGetOrIsAuthenticated
from .models import LikeButtonModel
# Create your views here.

User = get_user_model()
# Index of Blog and common for all
class IndexView(APIView):

    def get(self, request, *args, **kwargs):

        res_data = {
            'success': True,
            "message": 'Welcome to Edutech app !',
            'data': {}
        }
        return Response(res_data, status=status.HTTP_200_OK)

class BlogModelListView(APIView):
    # permission_classes = [IsGetOrIsAdmin]
    permission_classes = [IsAuthenticated]
    def get_userid(self, id):
        obj = None
        try:
            obj = UserProfile.objects.get(user=id)
            return obj
        except:
            obj=None
            return obj
        
    def get(self, request, *args, **kwargs):
     try:
        objects = BlogModel.objects.filter(is_deleted=False)
        serializer = BlogModelSerializer(objects, many=True)
      
        res_data = {
            'success': True,
            "message": 'Successfully listed all blogmodel',
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

    def post(self, request, *args, **kwargs):
        print("user :", request.user)
        id = request.user.id
        user_id= self.get_userid(id)
        post_data = request.data
        post_data.update({'user':user_id.id})
        serializer = BlogModelSerializer(data=request.data)
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

    def get_object(self, id):
        try:
            obj = BlogModel.objects.get(id=id)
            return obj
        except:
            obj=None
            return obj
    def put(self, request,id):
        try:
            userre = request.user
            user_id= self.get_userid(userre)
            print(user_id.id)
            post_data = request.data
            post_data.update({'user':user_id.id})
            object = self.get_object(id)
            serializer = BlogModelSerializer(object, data=request.data)
            create = object.created_by
            if create==userre:

                object = self.get_object(id)
                serializer = BlogModelSerializer(object, data=request.data)

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
                        "message": "Your not able to edit this post",
                        'data': str(ex)
                    }
                    return Response(res_data, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as ex:
            res_data = {
                'success': False,
                'message': 'Something went wrong',
                'data': str(ex)
            }
            return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        try:
            userre = request.user
            object = self.get_object(id)
            # object.delete()
            create = object.created_by
            if create == userre:
                object.is_deleted = True
                object.save()
                res_data = {
                    'success': True,
                    "message": "Post Successfully Deleted",
                    'data': None
                }
                return Response(res_data, status=status.HTTP_204_NO_CONTENT)
            else:
                res_data = {
                    'success': True,
                    "message": "Your not able to delete this post",
                    'data': None
                }
                return Response(res_data, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as ex:
            res_data = {
                'success': False,
                'message': 'Something went wrong',
                'data': str(ex)
            }
            return Response(res_data, status=status.HTTP_400_BAD_REQUEST)

class CommentBoxModelView(APIView):
    permission_classes = [IsAuthenticated]
    def get_userid(self, id):
        try:
            obj = UserProfile.objects.get(user=id)
            return obj
        except obj.DoesNotExist:
            return None
    def get(self, request,id, *args, **kwargs):
     try:
        objects = CommentBoxModel.objects.filter(is_deleted=False,post=id)
        serializer = CommentBoxModelSerializer(objects, many=True)
      
        res_data = {
            'success': True,
            "message": 'Successfully listed all comment',
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

    def post(self, request, *args, **kwargs):
        userre = request.user
        user_id= self.get_userid(userre)
        print(user_id.id)
        post_data = request.data
        post_data.update({'user':user_id.id})
        serializer = CommentBoxModelSerializer(data=request.data)
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

    def get_object(self, id):
        try:
            obj = CommentBoxModel.objects.get(id=id)
            return obj
        except obj.DoesNotExist:
            return None

    def put(self, request,id):
        try:
            object = self.get_object(id)
            serializer = CommentBoxEditModelSerializer(object, data=request.data)
            userre = request.user.id
            create = object.created_by.id
            print(userre)
            print(create)
            if create==userre:
                if serializer.is_valid(raise_exception=True):
                    obj = serializer.save()
                    obj.updated_by = request.user
                    obj.save()

                    res_data = {
                        'success': True,
                        "message": "Successfully Updated",
                        'data': serializer.data
                    }
                    return Response(res_data, status=status.HTTP_202_ACCEPTED)
                else:
                    res_data = {
                        'success': False,
                        "message": "comment Updated Failed",
                        'data': str(ex)
                    }
                    return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
            else:
                    res_data = {
                        'success': False,
                        "message": "comment Updated Failed",
                        'data': str(ex)
                    }
                    return Response(res_data, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as ex:
            res_data = {
                'success': False,
                'message': 'Your not able to edit this post',
                'data': str(ex)
            }
            return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, id):
        try:

            object = self.get_object(id)
            userre = request.user
            create = object.created_by
            if object is not None:
                if str(create) == str(userre):
                # object.delete()
                    object.is_deleted = True
                    object.save()
                    res_data = {
                        'success': True,
                        "message": "comment Successfully Deleted",
                        'data': None
                    }
                    return Response(res_data, status=status.HTTP_204_NO_CONTENT)
                else:
                    res_data = {
                        'success': False,
                        "message": "comment delete failed",
                        'data': str(ex)
                    }
                    return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
            else:
                res_data = {
                    'success': False,
                    "message": "comment delete failed",
                    'data': str(ex)
                }
                return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            res_data = {
                'success': False,
                'message': 'comment delete failed',
                'data': str(ex)
            }
            return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
        
class ChatView(APIView):
    permission_classes = [IsAuthenticated]
    def get_userid(self, id):
        try:
            obj = UserProfile.objects.get(user=id)
            return obj
        except obj.DoesNotExist:
            return None
    def get(self, request, *args, **kwargs):
     id = request.user
     user_id= self.get_userid(id)
     print(user_id.id)
     try:
        objects = ChatModel.objects.filter(is_deleted=False,to_user=user_id.id)
        serializer = ChatSerializer(objects, many=True)
      
        res_data = {
            'success': True,
            "message": 'Successfully listed all chat',
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

    def post(self, request,*args, **kwargs):
        user_obj =request.user
        from_user = UserProfile.objects.get(user=user_obj)
        post_data = request.data
        post_data.update({'from_user':from_user.id})
        to_user = post_data['to_user']
        print(to_user)
        serializer = ChatSendSerializer(data=post_data)
        if from_user.id != to_user:
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
                    "message": 'Message Creation Failed',
                    'data': serializer.errors
                }
                return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
        else:
                res_data = {
                    'success': False,
                    "message": 'No message',
                    'data': 'null'
                }
                return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
        
    def get_object(self, id):
        try:
            obj = ChatModel.objects.get(id=id)
            if obj.is_deleted==True:
                return None
            else:
                return obj    
        except obj.DoesNotExist:
            return None

    def put(self, request,id):
        try:
            object = self.get_object(id)
            serializer = ChatUpdateSerializer(object, data=request.data)
            userre = request.user
            create = object.created_by
            if create==userre:
                if serializer.is_valid(raise_exception=True):
                    obj = serializer.save()
                    obj.updated_by = request.user
                    obj.save()

                    res_data = {
                        'success': True,
                        "message": "Successfully Updated",
                        'data': serializer.data
                    }
                    return Response(res_data, status=status.HTTP_202_ACCEPTED)
                else:
                    res_data = {
                        'success': False,
                        "message": "comment Updated Failed",
                        'data': str(ex)
                    }
                    return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
            else:
                    res_data = {
                        'success': False,
                        "message": "comment Updated Failed",
                        'data': str(ex)
                    }
                    return Response(res_data, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as ex:
            res_data = {
                'success': False,
                'message': 'Your not able to edit this post',
                'data': str(ex)
            }
            return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, id):
        try:

            object = self.get_object(id)
            userre = request.user
            create = object.created_by
            if create==userre:
            # object.delete()
                object.is_deleted = True
                object.save()
                res_data = {
                    'success': True,
                    "message": "message Successfully Deleted",
                    'data': None
                }
                return Response(res_data, status=status.HTTP_204_NO_CONTENT)
            else:
                    res_data = {
                        'success': False,
                        "message": "message delete failed",
                        'data': str(ex)
                    }
                    return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            res_data = {
                'success': False,
                'message': 'message is already deleted',
                'data': None
            }
            return Response(res_data, status=status.HTTP_404_NOT_FOUND)






class likeCreateView(APIView):
    permission_classes = [IsAuthenticated]
        
    def post(self, request, *args, **kwargs):
        user_obj =request.user
        
        post_data = request.data
        post_data.update({'user':user_obj.id})
        obj_t = LikeButtonModel.objects.all()      
        serializer = LikeSerializer(data=post_data)
        
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
            blog_idd = post_data['blog_id']
            likes = LikeButtonModel.objects.get(user=user_id,blog_id=blog_idd)
            dislike = likes.is_liked
            print(dislike)


            if dislike == True:
                likes.is_liked = False
                print(likes.is_liked)
                likes.save()
                res_data = {
                    'success': True,
                    "message": 'Like change to dislike',
                    'data': None
                }
                return Response(res_data, status=status.HTTP_200_OK)
            

            elif dislike == False:
                likes.is_liked = True
                print(likes.is_liked)
                likes.save()
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


# Other Details Update View
class LikeDetailsByIDView(APIView):
    permission_classes = [IsGetOrIsAuthenticated]
    # parser_classes = (MultiPartParser, FormParser)

    def get_object(self, id):
        try:
            obj = BlogModel.objects.get(id=id)
            return obj
        except obj.DoesNotExist:
            return None

    def get(self, request, id):
        try:
            object = self.get_object(id)
            print(id)
            if object is not None:
                serializer = LikeButtonModel.objects.filter(is_liked=True,blog_id=id).count()
                print(serializer)
                res_data = {
                    'success': True, "message": 'Successuflly Fetched', 'data': serializer
                }
                return Response(res_data, status=status.HTTP_200_OK)
            else:
                res_data = {
                    'success': False, "message": 'Object not found', 'data': {}
                }
                return Response(res_data, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            res_data = {
                'success': False,
                'message': 'Something went wrong',
                'data': str(ex)
            }
            return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
        



class reportCreateView(APIView):
    permission_classes = [IsAuthenticated]
        
    def post(self, request, *args, **kwargs):
        user_obj =request.user
        
        post_data = request.data
        post_data.update({'user':user_obj.id})
        obj_t = reportBlog.objects.all()      
        serializer = reportSerializer(data=post_data)
        
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
        

class reportByIDView(APIView):
        def get(self, request, *args, **kwargs):
                try:
                    user_ob =request.user.id
                    objects = reportBlog.objects.filter(is_reported=True,user=user_ob)
                    serializer = reportSerializer(objects, many=True)
                
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