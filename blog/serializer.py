from asyncore import read
from rest_framework import serializers
from .models import *


class BlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = "__all__"
class CommentBoxModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CommentBoxModel
        fields = "__all__"
class CommentBoxEditModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CommentBoxModel
        fields = ['comment']
class ChatSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ChatModel
        fields = "__all__"

class ChatSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ChatModel
        fields = "__all__"

class ChatSendSerializer(serializers.ModelSerializer):
    message = serializers.CharField()
    class Meta:
        model = ChatModel
        fields = '__all__'
class ChatUpdateSerializer(serializers.ModelSerializer):
    message = serializers.CharField()
    

    class Meta:
        model = ChatModel
        fields = ['message']

class LikeSerializer(serializers.ModelSerializer):
    
    class Meta:
       
        model = LikeButtonModel
        fields = '__all__'

class reportSerializer(serializers.ModelSerializer):
    
    class Meta:
       
        model = reportBlog
        fields = '__all__'
         