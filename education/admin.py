from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

# University
class UniversityResource(resources.ModelResource):
    class Meta:
        model = UniversityModel

class UniversityAdmin(ImportExportModelAdmin):
    resource_class = UniversityResource
        
#Course
class CourseResource(resources.ModelResource):
    class Meta:
        model = CourseModel

class CourseAdmin(ImportExportModelAdmin):
    resource_class = CourseResource
        
admin.site.register(UniversityModel ,UniversityAdmin)
admin.site.register(CourseModel ,CourseAdmin)
admin.site.register(AboutModel)
admin.site.register(FeedModel)
admin.site.register(SlotModel)
admin.site.register(MCQInitialModel)
admin.site.register(NotificationModel)
admin.site.register(SyllabusModel)
admin.site.register(TeachContentModel)
admin.site.register(CaseStudyModel)
admin.site.register(Categories)
admin.site.register(BookMarks)
admin.site.register(reportBlog)
admin.site.register(galary)
admin.site.register(ApplicationModel)
admin.site.register(PaymentsModel)
admin.site.register(ApplicationSubmit)
