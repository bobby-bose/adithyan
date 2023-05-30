from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(BlogModel)
admin.site.register(CommentBoxModel)
admin.site.register(ChatModel)
admin.site.register(LikeButtonModel)