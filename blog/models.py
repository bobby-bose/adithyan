from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from django.contrib.auth import get_user_model
from authentication.models import *
def get_upload_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/Schema/media_uploads/user/user_id/filename.ext
    schema_name = "public"  # connection.get_schema()
    if instance.id:
        path = f"{schema_name}/media_uploads/crm/{instance.id}/{filename}"
    else:
        path = f"{schema_name}/media_uploads/crm/general/{filename}"
    return path

User = get_user_model()


class BlogModel(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name='blog_user')
    title = models.CharField(max_length=180,null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    url  = models.URLField(null=True, blank=True)
    attachements = models.FileField(upload_to=get_upload_directory_path, null=True, blank=True)
    type  = models.CharField(max_length=255,null=True, blank=True)
    image = models.ImageField(upload_to=get_upload_directory_path, null=True, blank=True)
    is_shown =  models.BooleanField(default=False)
    is_attended = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # Common Status field
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,
                                   related_name="blog_updated" )

    def __str__(self):
        return str(self.title)

    @property
    def slug_name(self):
        return "blog"
    
    class Meta:
        app_label = 'blog' 
    
    


class ChatModel(models.Model):
    from_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name='chat_from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_to_user')
    message = models.TextField(null=True, blank=True)
    is_read =  models.BooleanField(default=False)
    attachement = models.FileField(upload_to=get_upload_directory_path, null=True, blank=True)
    is_shown =  models.BooleanField(default=False)
    is_attended = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # Common Status field
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,
                                   related_name="chat_updated" )

    def __str__(self):
        return str(self.from_user)

    @property
    def slug_name(self):
        return "chat"
class CommentBoxModel(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING,related_name='commentbox_user')
    post = models.ForeignKey(BlogModel, null=True, blank=True, on_delete=models.DO_NOTHING,
                                    related_name="post_model")
    comment = models.TextField(null=True, blank=True)
    attachements = models.FileField(upload_to=get_upload_directory_path, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    is_shown =  models.BooleanField(default=False)
    is_attended = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # Common Status field
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,related_name="commentbox_created")
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,
                                    related_name="commentbox_updated")

    def __str__(self):
        return str(self.user.name)

    @property
    def slug_name(self):
        return "commentbox"
    

class LikeButtonModel(models.Model):
    TYPES =  [("BG", "blog"), ("CT", "Chat")]
    model_name =models.CharField(max_length=180, null=True, blank=True, choices=TYPES, default="BG")
    user = models.CharField(max_length=255)
    blog_id = models.CharField(max_length=255)
    is_liked =  models.BooleanField(default=False)
    is_attended = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # Common Status field
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,related_name="like_created")
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,
                                  related_name="like_updated")

    def __str__(self):
        return str(self.id)

    @property
    def slug_name(self):
        return "likebutton"
    class Meta:
        unique_together = ('model_name', 'user', 'blog_id')



class reportBlog(models.Model):
    TYPES =  [("BG", "blog"), ("CT", "Chat")]
    model_name =models.CharField(max_length=180, null=True, blank=True, choices=TYPES, default="BG")
    user = models.CharField(max_length=255)
    blog_id = models.CharField(max_length=255)
    is_reported =  models.BooleanField(default=False)
    is_attended = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # Common Status field
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,related_name="Report_created")
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,
                                  related_name="Report_updated")
    
    def __str__(self):
        return str(self.id)

    @property
    def slug_name(self):
        return "likebutton"
    class Meta:
        unique_together = ('model_name', 'user', 'blog_id')



