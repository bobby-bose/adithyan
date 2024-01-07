# API/User/Views.
import json
from random import *
from django.http import HttpResponse
from rest_framework import status, generics, mixins, parsers, renderers
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework.response import Response
from .serializers import * 
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import UserProfile
from django.db.models import Q
from .serializers import *
from twilio.rest import Client
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserData, Question, Notification
from .serializers import UserDataSerializer, QuestionSerializer, NotificationSerializer
import datetime

def index(request):
    return HttpResponse("Welcome to CORE App API Portal")


# Send Generated OTP to User mobile via SMS
def send_otp_mobile(otp,mobile):
    account_sid = 'ACb2e5c320c3f02b2d7f1b973d305827fb'
    auth_token = '7a848fbd5e448c80f80c7281990d8c09'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='+16203373752',
    body='your otp is '+str(otp),
    to = '+'+ str(mobile)
    )
    return True

# Register API
class RegisterAPI(APIView):
    # serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def get_user(self, username):
        obj=None
        try:
            obj = User.objects.get(username=username)
            return obj
        except:
            obj=None
            return obj

    def post(self, request, *args, **kwargs):
        try:
      
            # serializer = self.get_serializer(data=request.data)
            # serializer.is_valid(raise_exception=True)
            json_data = json.loads(request.body)
            country_code = str(json_data.get("country_code"))
            mobile = str(json_data.get("mobile"))
            new_mobile = mobile.replace(" ", "")
            email = str(json_data.get("email"))
            username = str(country_code)+str(new_mobile)
            obj = self.get_user(username)
            print(username)
            if obj is None:
                user = User.objects.create(username=username,email=email)
                print(user)
                # password =  randint(100001, 999999)
                password=123456
                # send_sms = send_otp_mobile(password,username)
                # print(send_sms)
                user.set_password(str(password))
                user.save()
                profile = UserProfile.objects.create(user=user, otp=password, mobile=username)
                res_data = {
                    "success": True,
                    "message": "Registration Successfull, OTP has been to send your mobile number",
                    "data": {
                        "id" : profile.id,
                        "username" : user.username
                    }
                }
                return Response(res_data, status=status.HTTP_201_CREATED)
            else:
                user = User.objects.get(username=username)
                if user is None:
                    res_data = {"code":404, "success":False, "data": {}, "message": "User Not Registerd with give Phone number"}
                    return Response(res_data, status=status.HTTP_404_NOT_FOUND)
            
                password =  123456
                # send_sms = send_otp_mobile(password,username)
                # print(send_sms)
                user.set_password(str(password))
                user.save()
                user_profile = UserProfile.objects.get(user=user)
                user_profile.otp = password
                user_profile.save()
                res_data = {
                    'code' : 200,
                    'success': True,
                    'message': 'OTP Send to Successfully',
                    'data': {'id': user.id,
                            'username': user.username,
                            'scope': ""
                            },
                }
                return Response(res_data, status=status.HTTP_200_OK)
        except Exception as ex:
            res_data = {
                "success": False,
                "message": " Something went wrong !",
                "data": str(ex),
            }
            return Response(res_data, status=status.HTTP_400_BAD_REQUEST)

from rest_framework_simplejwt.tokens import RefreshToken





class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        try:
            country_code = request.data.get('country_code')
            mobile_number = request.data.get('mobile_number')

            if not country_code or not mobile_number:
                raise ValueError('Both country_code and mobile_number are required.')

            mobile = f"{country_code}{mobile_number}"
            print(mobile)
            user_obj=User.objects.get(username=mobile)
            print(user_obj)

            # Generate JWT tokens
            refresh = RefreshToken.for_user(user_obj)
            access = str(refresh.access_token)

            res_data = {
                'code': 200,
                'success': True,
                'message': 'User login Successfully',
                'data': {
                    'id': user_obj.id,
                    'mobile_number': user_obj.username,
                },
                'token': {'access': access, 'refresh': str(refresh)}
            }
            return Response(res_data, status=status.HTTP_200_OK)
        except Exception as ex:
            res_data = {
                'code': 400,
                'success': False,
                'message': 'Invalid Mobile Number or Password',
                'data': str(ex),
                'token': None
            }
            return Response(res_data, status=status.HTTP_401_UNAUTHORIZED)




class PreLoginView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class=LoginSerializer

    def post(self, request):
        try:
            json_data = json.loads(request.body)
            country_code = str(json_data.get("country_code"))
            mobile = str(json_data.get("mobile"))
            username = str(country_code) + str(mobile)
            user = User.objects.filter(username=username).first()

            if user is None:
                res_data = {"code": 404, "success": False, "data": {}, "message": "User Not Registered with the given Phone number"}
                return Response(res_data, status=status.HTTP_404_NOT_FOUND)

            password = randint(100001, 999999)
            send_sms = send_otp_mobile(password, username)
            print(password)

            user.set_password(str(password))
            user.save()

            user_profile, created = UserProfile.objects.get_or_create(user=user)
            user_profile.otp = password
            user_profile.save()

            res_data = {
                'code': 200,
                'success': True,
                'message': 'OTP Sent Successfully',
                'data': {'id': user.id,  # Corrected from user_obj to user
                         'username': user.username,
                         'scope': ""
                         },
            }
            return Response(res_data, status=status.HTTP_200_OK)
        except Exception as ex:
            res_data = {
                'code': 400,
                'success': False,
                'message': 'Invalid Username',
                'data': str(ex),
                'token': None
            }
            return Response(res_data, status=status.HTTP_400_BAD_REQUEST)


# Logout View
class LogoutView(APIView):
    permission_classes = (IsAuthenticated)
    serializer_class=LoginSerializer

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            res_data = {
                'success': True,
                'message': 'Successfully Logout',
                'data': {}
            }
            return Response(res_data, status=status.HTTP_205_RESET_CONTENT)
        except Exception as ex:
            res_data = {
                'success': False,
                'message': 'Something went wrong',
                'data': str(ex)
            }
            return Response(res_data, status=status.HTTP_400_BAD_REQUEST)


# Logout from ALl devices
class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)
        return Response(status=status.HTTP_205_RESET_CONTENT)


# Change Password for Logined user
class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                res_data = {
                    'success': True,
                    'message': 'Password updated successfully',
                    'data': serializer.data
                }
                return Response(res_data, status=status.HTTP_200_OK)

            else:
                res_data = {
                    'success': False,
                    "message": "Password Updation failed",
                    'data': str(serializer.errors),
                }
                return Response(res_data, status=status.HTTP_406_NOT_ACCEPTABLE)


        except Exception as ex:
            res_data = {
                'success': False,
                "message": "Password Updation failed",
                'data': str(ex),
            }
            return Response(res_data, status=status.HTTP_406_NOT_ACCEPTABLE)

class AddNotificationAPIView(APIView):
    serializer_class=NotificationSerializer
    def post(self, request, *args, **kwargs):
        try:
            serializer = NotificationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class AddQuestionAPIView(APIView):
    serializer_class = QuestionSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = QuestionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, *args, **kwargs):
        try:
            questions = Question.objects.all()
            serializer = QuestionSerializer(questions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class HomePageAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            # Get the current date and time
            current_datetime = datetime.datetime.now()

            # Create a new datetime object with the same year and month, and set the day to 1
            first_day_of_month = current_datetime.replace(day=6)
            print(first_day_of_month)

            # Get the question of the day based on the date
            question_of_the_day = Question.objects.get(day_of_month=first_day_of_month)
            question_serializer = QuestionSerializer(question_of_the_day)

            # Get all notifications
            all_notifications = Notification.objects.all()
            all_notifications_serializer = NotificationSerializer(all_notifications, many=True)

            # Get offer notifications
            offer_notifications = Notification.objects.filter(notification_type='OFFERS')
            offer_notifications_serializer = NotificationSerializer(offer_notifications, many=True)

            response_data = {
                'question_of_the_day': question_serializer.data,
                'all_notifications': all_notifications_serializer.data,
                'offer_notifications': offer_notifications_serializer.data,
            }

            return Response(response_data, status=status.HTTP_200_OK)

        except Question.DoesNotExist:
            return Response({'error': 'Question of the day not found.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        try:
            mood = request.data.get('mood', '')
            mcq_answer = request.data.get('mcq_answer', '')  # Assuming 'mcq_answer' is the field name

            if not mood:
                return Response({'error': 'Mood is required.'}, status=status.HTTP_400_BAD_REQUEST)

            # Save mood to the user's data model
            user_data, created = UserData.objects.get_or_create(user=request.user)
            user_data.mood = mood
            user_data.save()

            # Get the day of the month
            day_of_month = datetime.datetime.now().day

            # Get the question of the day based on the date
            question_of_the_day = Question.objects.get(day_of_month=day_of_month)

            # Save MCQ answer to the user's data model
            user_data.mcq_answer = mcq_answer
            user_data.save()

            response_data = {
                'mood_data': UserDataSerializer(user_data).data,
                'question_of_the_day': QuestionSerializer(question_of_the_day).data,
            }

            return Response(response_data, status=status.HTTP_200_OK)

        except Question.DoesNotExist:
            return Response({'error': 'Question of the day not found.'}, status=status.HTTP_404_NOT_FOUND)

        except UserData.DoesNotExist:
            return Response({'error': 'User data not found.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)







# API View for  Retrieve User data, Update and delete User data using pk as ID
# ( For logines user only)
class UserProfileAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        try:
            id = request.user.id
            user_obj = self.get_object(id)
            serializer = UserProfileSerializer(user_obj)
            res_data = {
                'success': True,
                "message": 'User details fetched Successfully',
                'data': serializer.data
            }
            return Response(res_data, status=status.HTTP_200_OK)
        except Exception as ex:
            res_data = {
                'success': False,
                'message': 'Invaild Username or Password',
                'data': str(ex)
            }
            return Response(res_data, status=status.HTTP_406_NOT_ACCEPTABLE)

    def put(self, request):
        id = request.user.id
        user_obj = self.get_object(id)
        serializer = UserSerializer(user_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            res_data = {
                'success': True,
                "message": 'Successfully Updated',
                'data': serializer.data
            }
            return Response(res_data, status=status.HTTP_202_ACCEPTED)
        else:
            res_data = {
                'success': False,
                "message": "User Updating failed",
                'data': str(serializer.errors)
            }
            return Response(res_data, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request):
        try:
            id = request.user.id
            user_obj = self.get_object(id)
            user_obj.delete()
            res_data = {
                'success': True,
                "message": 'Successfully Deleted',
                'data': None
            }
            return Response(res_data, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            res_data = {
                'success': False,
                'message': 'Invaild Username or Password',
                'data': str(ex)
            }
            return Response(res_data, status=status.HTTP_406_NOT_ACCEPTABLE)


# Get a user profile by Entering User ID
class UserDetailById(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        user_obj = self.get_object(id)
        # serializer = UserSerializer(user_obj)
        serializer = DetailedUserSerializer(user_obj)
        res_data = {
            'success': True,
            "message": 'User details fetched Successfully',
            'data': serializer.data
        }
        return Response(res_data, status=status.HTTP_200_OK)

    def put(self, request, id):
        user_obj = self.get_object(id)
        serializer = UserSerializer(user_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            res_data = {
                'success': True,
                "message": 'Successfully Updated',
                'data': serializer.data
            }
            return Response(res_data, status=status.HTTP_202_ACCEPTED)
        else:
            res_data = {
                'success': False,
                "message": "User Updating failed",
                'data': str(serializer.errors)
            }
            return Response(res_data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            user_obj = self.get_object(id)
            #user_obj.delete()
            user_obj.is_deleted = True
            user_obj.save()
            res_data = {
                'success': True,
                "message": 'Successfully Deleted',
                'data': None
            }
            return Response(res_data, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            res_data = {
                'success': False,
                'message': 'Invaild Username or Password',
                'data': str(ex)
            }
            return Response(res_data, status=status.HTTP_400_BAD_REQUEST)


# Django REST API with serializer - For List Userss
class UserListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Added filter and Sorting
        query = request.GET.get('query', '')
        sort_param = request.GET.get('sort_param', '')
        sort_type = request.GET.get('sort_type', '')
        if sort_type and sort_type == "asc":
            if sort_param:
                ordering = str(sort_param)
            else:
                ordering = "id"
        else:
            if sort_param:
                ordering = "-" + str(sort_param)
            else:
                ordering = "-id"
        # user_objects = User.objects.all()
        user_objects = User.objects.filter(
            Q(username_icontains=query) | Q(first_nameicontains=query) | Q(last_name_icontains=query),
            is_staff=False, is_deleted=False).order_by(ordering)
        serializer = UserListSerializer(user_objects, many=True)
        res_data = {
            'success': True,
            "message": 'Success fully listed all users',
            'data': serializer.data
        }
        return Response(res_data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            res_data = {
                'success': True,
                "message": 'Success',
                'data': serializer.data
            }
            return Response(res_data, status=status.HTTP_201_CREATED)
        res_data = {
            'success': False,
            "message": "User Creation Error",
            'data': str(serializer.errors)
        }
        return Response(res_data, status=status.HTTP_400_BAD_REQUEST)

class MoodView(APIView):
    # permission_classes = [IsGetOrIsAdmin]
    
    def get_object(self,id):
        try:
            return UserProfile.objects.get(user=id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def put(self, request):
        try:
            id = request.user
            object = self.get_object(id)
            serializer = MoodSerializer(object, data=request.data)
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
                    'data': str(serializer.errors)
                }
                return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            res_data = {
                'success': False,
                'message': 'Something went wrong',
                'data': str(ex)
            }
            return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
     try:
        objects = UserProfile.objects.all()
        serializer = MoodlistSerializer(objects, many=True)
      
        res_data = {
            'success': True,
            "message": 'Successfully listed all User',
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
class UserProfileUpdate(APIView):
    def get_object(self,id):
        try:
            return UserProfile.objects.get(user=id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def put(self, request):
        try:
            id=request.user.id
            object = self.get_object(id)
            serializer = UserProfileUpdateSerializer(object, data=request.data)
            userre = request.user
            create = object.user
            if create==userre:
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
                        'data': str(serializer.errors)
                    }
                    return Response(res_data, status=status.HTTP_400_BAD_REQUEST)
            else:
                    res_data = {
                        'success': False,
                        "message": "Department Updation failed",
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
    def get(self, request, *args, **kwargs):
     try:
        objects = UserProfile.objects.all()
        serializer = UserProfileUpdateSerializer(objects, many=True)
      
        res_data = {
            'success': True,
            "message": 'Successfully listed all User',
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
     
class SearchApi(APIView):
    

    # def get_queryset(self,request):
    #     queryset = super().get_queryset()
    #     # Get the search term from the request query parameters
    #     search_term = self.request.query_params.get('name')
    #     if search_term:
    #         # Perform the search using case-insensitive matching on title and author fields
    #         queryset = queryset.filter(models.Q(name__icontains=search_term) )
    #         res_data = {
    #         'success': True,
    #         "message": 'Successfully listed all User',
    #         'data': search_term.data
    #     }
    #         return Response(res_data, status=status.HTTP_200_OK)
    def get(self, request):
        # Added filter and Sorting
        try:
            query = request.GET.get('query', '')
            user_objects = UserProfile.objects.filter(Q(name__icontains=query)).order_by('-id')
            serializer = UserProfileSerializer(user_objects, many=True)
            res_data = {
                'success': True,
                "message": 'Success fully listed all users',
                'data': serializer.data
            }
            return Response(res_data, status=status.HTTP_200_OK)
        except Exception as ex:
           
            res_data = {
                'success': False,
                "message": 'Some thing went wrong',
                'data':str(ex)
            }
            return Response(res_data, status=status.HTTP_400_BAD_REQUEST)