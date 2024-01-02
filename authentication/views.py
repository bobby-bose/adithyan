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
from .models import CustomUser

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
            if obj is None:
                user = User.objects.create(username=username,email=email)
                password =  randint(100001, 999999)
                send_sms = send_otp_mobile(password,username)
                print(send_sms)
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
            
                password =  randint(100001, 999999)
                send_sms = send_otp_mobile(password,username)
                print(send_sms)
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

def get_tokens_for_user(mobile_number):
    # Your logic to get or create user and generate tokens
    # This is just a basic example; you may need to customize it based on your authentication logic
    
    user = CustomUser.objects.get(mobile_number=mobile_number)
    
    refresh = RefreshToken.for_user(user)

    return {
        'access': str(refresh.access_token),
        'refresh': str(refresh),
    }

def get_tokens_for_user(mobile_number):
    # This is a simplified example, you may want to use a library like `dj-rest-auth` for token generation
    # In this example, we are assuming you have a function to generate tokens called `generate_tokens`
    access_token, refresh_token = generate_tokens(mobile_number)
    return {"access": access_token, "refresh": refresh_token}

def generate_tokens(mobile_number):
    # Replace this with your actual token generation logic
    # This is a simplified example, you may use Django Rest Framework's `Token` model or JWT library
    return "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFydGh5IiwidXNlcl9pZCI6MiwibmJmIjoxNjA5NTk1NzIyLCJleHAiOjE2MDk2MDk3MjIsImlhdCI6MTYwOTU5NTcyMn0.XtJLJ2zwXT2H5tz4V4U4LXfqh7J9jiN2edY99esRwSk", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImJvYmJ5IiwidXNlcl9pZCI6MSwiZXhwIjoxNTE2MjM5MDIyfQ.O9y-njdEaJx3nXhPLG69e62Z52ezhj3uHefhBeWg6o0"

def get_or_create_user(mobile_number):
    # Get the user model
    User = get_user_model()

    # Try to get the user by mobile number
    user, created = User.objects.get_or_create(mobile_number=mobile_number, defaults={"password": "Password@37", "username": "bobby"})
    return user, created

def get_or_create_user(mobile_number):
    # Get the user model

    # Try to get the user by mobile number
    user, created = CustomUser.objects.get_or_create(mobile_number=mobile_number, defaults={"password": "Password@37", "username": "bobby"})
    return user, created

@permission_classes((AllowAny,))
class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)

            mobile_number = serializer.validated_data['mobile_number']

            # Assuming 'get_tokens_for_user' is a function to generate tokens for a user
            custom_token = get_tokens_for_user(mobile_number)
            access = custom_token.get("access")
            refresh = custom_token.get("refresh")

            # Assuming 'get_or_create_user' is a function to create a user if not exists
            user_obj, created = get_or_create_user(mobile_number)

            user_scop = user_obj.user_scop  # Accessing user_scop directly from the CustomUser instance

            res_data = {
                'code': 200,
                'success': True,
                'message': 'User login Successfully',
                'data': {'id': user_obj.id,
                         'mobile_number': user_obj.mobile_number,
                         'scope': user_scop
                         },
                'token': {'access': access, 'refresh': refresh}
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