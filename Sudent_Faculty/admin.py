from django.contrib import admin
from .models import Student_info,Admission,marks,Stu_Feedback

class Stuent_info_Admin(admin.ModelAdmin):
    list_per_page=10
    list_display = ['Studentname','image','RegNO','address','District','pincode']
admin.site.register(Student_info,Stuent_info_Admin)

class AdmissionAdmin(admin.ModelAdmin):
    list_per_page = 10

    # exclude = ['user']

    list_display = ['regNO','nameStudent','Class','branch','Date_Admission']

    # def save_model(self, request, obj, form, change):
    #     obj.user = request.user
    #     obj.save()


admin.site.register(Admission,AdmissionAdmin)



class marksAdmin(admin.ModelAdmin):
    list_per_page=10
    list_display = ['regNO','Totalmarks','Semester','Year']

#    exclude = ['user']


    # def save_model(self, request, obj, form, change):
    #     obj.user = request.user
    #     obj.save()


admin.site.register(marks, marksAdmin)


# Student : ['user','student_name','City','address','branch','education','experience']

class FeedbackAdmin(admin.ModelAdmin):
    list_per_page=10
    list_display = ['regNO', 'date', 'Subject','Feedback_stu']

    # exclude = ['user']
    # def save_model(self, request, obj, form, change):
    #     obj.user = request.user
    #     obj.save()
admin.site.register(Stu_Feedback,FeedbackAdmin)
   