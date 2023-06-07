from django.db import models
from django.contrib.auth import get_user_model
from blog.models import *
from django.contrib.auth import get_user_model
from authentication.models import UserProfile
User = get_user_model()
# from autoslug import AutoSlugField
import uuid

# Create your models here.
#auth

def get_upload_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/Schema/media_uploads/user/user_id/filename.ext
    schema_name = "public"  # connection.get_schema()
    if instance.id:
        path = f"{schema_name}/media_uploads/crm/{instance.id}/{filename}"
    else:
        path = f"{schema_name}/media_uploads/crm/general/{filename}"
    return path
#blog

class AuditTablesModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name='audit_user')
    activity =  models.CharField(max_length=180,null=True, blank=True)
    otp = models.CharField(max_length=6,unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)  # Common Status field
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='audit_created')



    def __str__(self):
        return str(self.user.name)

    @property
    def slug_name(self):
        return "audittables"

class NotificationModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name='notification_user')
    title = models.CharField(max_length=180,null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    is_offer = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # Common Status field
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,related_name='notification_created')
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,
                                   related_name='notification_updated')

    def __str__(self):
        return str(self.user)

    @property
    def slug_name(self):
        return "notification"


class MessageModel(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING , related_name='message_user')
    title = models.CharField(max_length=180,null=True, blank=True)
    message = models.CharField(max_length=180,null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    type = models.CharField(max_length=180,null=True, blank=True )
    is_read = models.BooleanField(default=False)
    attachement = models.FileField(upload_to=get_upload_directory_path, null=True, blank=True)
    is_active = models.BooleanField(default=True)  # Common Status field
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,related_name= 'message_created')
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,
                                    related_name= 'message_updated')

    def __str__(self):
        return str(self.user.name)

    @property
    def slug_name(self):
        return "Message"

class MCQInitialModel(models.Model):
    question = models.TextField(null=True, blank=True)
    option_1 = models.CharField(max_length=180,null=True, blank=True)
    option_2 = models.CharField(max_length=180,null=True, blank=True)
    option_3 = models.CharField(max_length=180,null=True, blank=True)
    option_4 = models.CharField(max_length=180,null=True, blank=True)
    answer = models.CharField(max_length=180,null=True, blank=True)
    is_shown =  models.BooleanField(default=False)
    is_attended = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # Common Status field
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,related_name= 'mcqInitial_created')
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,
                                    related_name= 'mcqInitial_updated')

    def __str__(self):
        return str(self.question)

    @property
    def slug_name(self):
        return "mcqInitial"

class UniversityModel(models.Model):
    univesity_name=models.CharField(max_length=255)
    location = models.CharField(max_length=180,null=True, blank=True)
    established_year = models.CharField(max_length=180,null=True, blank=True)
    ranking = models.CharField(max_length=180,null=True, blank=True)
    bookmark = models.BooleanField(default=False)
    contry = models.CharField(max_length=180,null=True, blank=True)
    type = models.CharField(max_length=180,null=True, blank=True)
    code = models.CharField(max_length=255,blank=True)
   
    url = models.URLField(null=True, blank=True)
    is_shown =  models.BooleanField(default=False)
    is_attended = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # Common Status field
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,related_name='university_created')
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,
                                   related_name='univesity_updated' )

    def __str__(self):
        return str(self.univesity_name)

    @property
    def slug_name(self):
        return "university"


class CourseModel(models.Model):
    course_name = models.CharField(max_length=180,null=True, blank=True)
    univesity_name = models.ForeignKey(UniversityModel, null=True, blank=True, on_delete=models.DO_NOTHING,
                                   related_name='course_univesity_name')
    location = models.CharField(max_length=180,null=True, blank=True)
    course_duration = models.CharField(max_length=180,null=True, blank=True)
    intake = models.CharField(max_length=180,null=True, blank=True)
    bookmark = models.BooleanField(default=False)
    fees_1   = models.CharField(max_length=180,null=True, blank=True)
    fees_2   = models.CharField(max_length=180,null=True, blank=True)
    fees_3  = models.CharField(max_length=180,null=True, blank=True)
    fees_4   = models.CharField(max_length=180,null=True, blank=True)
    fees_5  = models.CharField(max_length=180,null=True, blank=True)
    fees_6  = models.CharField(max_length=180,null=True, blank=True)
    neet = models.BooleanField(default=False)
    ielts = models.BooleanField(default=False)
    passport = models.BooleanField(default=False)
    tenth_cert = models.BooleanField(default=False)
    twelveth_cert = models.BooleanField(default=False)
    visa = models.BooleanField(default=False)
    remarks =  models.CharField(max_length=180,null=True, blank=True)
    url = url = models.URLField(null=True, blank=True)
    code =  models.CharField(max_length=180,null=True, blank=True)
    is_shown =  models.BooleanField(default=False)
    is_attended = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # Common Status field
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,related_name='course_create')
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,
                                   related_name='course_update' )

    def __str__(self):
        return str(self.course_name)

    @property
    def slug_name(self):
        return "course"

class AboutModel(models.Model):
    univesity_name = models.ForeignKey(UniversityModel, null=True, blank=True, on_delete=models.DO_NOTHING,
                                   related_name='about_univesity_name')
    about  = models.TextField(null=True, blank=True)
    ranking = models.CharField(max_length=225,null=True, blank=True)
    no_of_program = models.IntegerField(null=True,blank=True,default=0)
    FMGE = models.BooleanField(default=False)
    USML = models.BooleanField(default=False)
    PLAB = models.BooleanField(default=False)
    library =  models.BooleanField(default=False)
    accomodation = models.BooleanField(default=False)
    class_rooms = models.BooleanField(default=False)
    laboratories = models.BooleanField(default=False)
    clinic  = models.BooleanField(default=False)
    play_grount = models.BooleanField(default=False)
    is_shown =  models.BooleanField(default=False)
    is_attended = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # Common Status field
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,related_name='about_created')
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,
                                    related_name='about_update')

    def __str__(self):
        return str(self.about)

    @property
    def slug_name(self):
        return "about"



class FeedModel(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING,related_name='feed_user')
    feed_title = models.CharField(max_length=180,null=True, blank=True)
    feed = models.TextField(null=True, blank=True)
    univesity_name = models.ForeignKey(UniversityModel, null=True, blank=True, on_delete=models.DO_NOTHING,
                                   related_name='feed_univesity_name')
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_shown =  models.BooleanField(default=False)
    is_attended = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # Common Status field
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,related_name='feed_create')
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,
                                   related_name='feed_update')

    def __str__(self):
        return str(self.user)

    @property
    def slug_name(self):
        return "feed"


class SlotModel(models.Model):
    timings = models.CharField(max_length=225,null=True, blank=True)
    is_booked = models.BooleanField(default=False)
    date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    slot_id = models.CharField(max_length=180,null=True, blank=True)
    consultant = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="slotmodel_user")
    student = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING, related_name='slot_student')
    is_shown =  models.BooleanField(default=False)
    is_attended = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # Common Status field
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,related_name="slot_created")
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,
                                 related_name="slot_updated")

    def __str__(self):
        return str(self.timings)

    @property
    def slug_name(self):
        return "slot"





class BookMarks(models.Model):
    TYPES =[("UN", "university"), ("CS", "course"), ("BL", "blog")]
    user = models.CharField(max_length=180,null=True, blank=True)
    obj_id = models.CharField(max_length=180,null=True, blank=True)
    slug = models.CharField(max_length=180, null=True, blank=True, choices=TYPES,)
    book_mark = models.BooleanField(default=False)
    is_shown =  models.BooleanField(default=False)
    is_attended = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # Common Status field
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,related_name="bookmarks_created")
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,
                                  related_name="bookmarks_updated")

    def __str__(self):
        return str(self.id)

    class Meta:
        unique_together = ('obj_id', 'user', 'slug')

class ApplicationModel(models.Model):
    step_1 = models.BooleanField(default=False)
    step_2 = models.BooleanField(default=False)
    step_3 = models.BooleanField(default=False)
    step_4 = models.BooleanField(default=False)
    step_5 = models.BooleanField(default=False)
    step_6 = models.BooleanField(default=False)
    course = models.ForeignKey(CourseModel, on_delete=models.DO_NOTHING,related_name="application_course")
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name="application_user")
    is_shown =  models.BooleanField(default=False)
    is_attended = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # Common Status field
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,related_name="application_created" )
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,
                                   related_name="application_updated")

    def __str__(self):
        return str(self.user)

    @property
    def slug_name(self):
        return "application"

class SyllabusModel(models.Model):
    course = models.ForeignKey(CourseModel, on_delete=models.DO_NOTHING,related_name="course")
    topic_count = models.IntegerField(null=True, blank=True,)
    content_count = models.IntegerField(null=True, blank=True,)
    subject_code = models.CharField(max_length=180, null=True, blank=True,)
    subject_name = models.CharField(max_length=180, null=True, blank=True,)
    point = models.IntegerField(null=True, blank=True,)
    year = models.IntegerField(null=True, blank=True,)
    url = models.URLField(null=True, blank=True)
    remarks = models.CharField(max_length=180, null=True, blank=True,)
    is_premium = models.BooleanField(default=False)
    is_shown =  models.BooleanField(default=False)
    is_attended = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # Common Status field
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,related_name="syllabus_created")
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,
                                   related_name="syllabus_updated")

    def __str__(self):
        return str(self.course)

    @property
    def slug_name(self):
        return "syllabus"

class Categories(models.Model):
    main_cat = [("video", "Video"), ("mcq", "MCQ"), ("clinical-case", "Clinical Case"), ("q-bank", "Q-bank"), ("flash-card", "Flash card")]
    main_catogory = models.CharField(max_length=180, null=True, blank=True, choices=main_cat,default=None)
    sub_catogory = models.CharField(max_length=180, null=True, blank=True)
    catogory_id = models.CharField(max_length=120, null=True, blank=True, unique=True)
    is_premium = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # Common Status field
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.sub_catogory) + " - " + str(self.catogory_id)


class TeachContentModel(models.Model):
    catogory = models.ForeignKey(Categories,on_delete=models.DO_NOTHING, null=True, blank=True,)
    title = models.CharField(max_length=180, null=True, blank=True,)
    thumbnail = models.ImageField(upload_to=get_upload_directory_path, null=True, blank=True)
    duration =  models.CharField(max_length=180, null=True, blank=True,)
    is_premium = models.BooleanField(default=True)
    auther = models.CharField(max_length=180, null=True, blank=True,)
    type = models.CharField(max_length=180, null=True, blank=True,)
    video_url = models.URLField(null=True, blank=True)
    file = models.FileField(upload_to=get_upload_directory_path, null=True, blank=True)
    image = models.ImageField(upload_to=get_upload_directory_path, null=True, blank=True)
    discription = models.CharField(max_length=255, null=True, blank=True,)
    question = models.CharField(max_length=255, null=True, blank=True,)
    option_1 = models.CharField(max_length=255, null=True, blank=True,)
    option_2 = models.CharField(max_length=255, null=True, blank=True,)
    option_3 = models.CharField(max_length=255, null=True, blank=True,)
    option_4 = models.CharField(max_length=255, null=True, blank=True,)
    answer = models.CharField(max_length=255, null=True, blank=True,)
    galary = models.ImageField(upload_to=get_upload_directory_path, null=True, blank=True)
    is_premium = models.BooleanField(default=False)
    is_shown =  models.BooleanField(default=False)
    is_attended = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # Common Status field
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,related_name="teachcontent_created")
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,
                                related_name="teachcontent_updated")
    
    # slug = models.SlugField(choices=TYPES,
    #                    unique=True,null=True,default=None)
    def __str__(self):
        return str(self.title)

    @property
    def slug_name(self):
        return "teachcontent"

class CaseStudyModel(models.Model):
    TYPES =[("", ""), ("", ""), ("", "")]
    Description = models.CharField(max_length=255, null=True, blank=True,)
    Topic = models.CharField(max_length=180, null=True, blank=True, choices=TYPES,)
    content = models.CharField(max_length=255, null=True, blank=True,)
    Titles = models.CharField(max_length=255, null=True, blank=True,)
    url = models.URLField(null=True, blank=True)
    attachment = models.FileField(upload_to=get_upload_directory_path, null=True, blank=True)
    image = models.ImageField(upload_to=get_upload_directory_path, null=True, blank=True)
    is_shown =  models.BooleanField(default=False)
    is_attended = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # Common Status field
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,related_name="casestudy_ctreated")
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,
                                  related_name="casestudy_updated")

    def __str__(self):
        return str(self.Topic)

    @property
    def slug_name(self):
        return "casestudy"

class PackageModel(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True,)
    validity = models.IntegerField(null=True, blank=True,)
    exp_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    Permission = models.JSONField(null=True,default=dict)
    is_shown =  models.BooleanField(default=False)
    is_attended = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # Common Status field
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,related_name="package_created")
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,
                                    related_name="package_updated")

    def __str__(self):
        return str(self.name)

    @property
    def slug_name(self):
        return "package"

class PaymentsModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name='payments_user')
    amount = models.FloatField(null=True, blank=True)
    transetion_id = models.CharField(max_length=255, null=True, blank=True,)
    date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    order_id = models.CharField(max_length=255, null=True, blank=True,)
    is_compleete = models.BooleanField(default=False)
    Bank_ref = models.CharField(max_length=255, null=True, blank=True,)
    remarks = models.CharField(max_length=255, null=True, blank=True,)
    is_shown =  models.BooleanField(default=False)
    is_attended = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # Common Status field
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,related_name="payments_created")
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,
                                   related_name="payments_updated")

    def __str__(self):
        return str(self.user)

    @property
    def slug_name(self):
        return "payments"
    



class galary(models.Model):
    TYPES =  [("UN", "univesity"), ("Nl", "null")]
    model_name =models.CharField(max_length=180, null=True, blank=True, choices=TYPES, default="BG")
    univesity_id = models.ForeignKey(UniversityModel , on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name='galary_user')
    image = models.ImageField(upload_to=get_upload_directory_path, null=True, blank=True)
    model_object = models.CharField(max_length=255)
    image_uuid = models.UUIDField(null=True, default=uuid.uuid4, unique=True)
    image_type = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)  # Common Status field
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,related_name="galary_created")
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,
                                  related_name="galary_updated")



class ApplicationSubmit(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name='applicationsubmit_user')
    univesity_id = models.ForeignKey(UniversityModel , on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.DO_NOTHING,related_name="applicationsubmit_course")
    month = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    email_id = models.EmailField(max_length=255)
    is_active = models.BooleanField(default=True)  # Common Status field
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,related_name="applicationsubmit_created")
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,
                                  related_name="Application_updated")
    
    class Meta:
        unique_together = ('univesity_id', 'user', 'course')
