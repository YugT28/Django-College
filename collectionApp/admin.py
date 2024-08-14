from django.contrib import admin
from .models import Student,Faculty,Course,Branch,Result

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['Sid','Sname','Sdob','Syear','Bid']
    list_select_related = ['Bid']
    class Meta:
        model = Student
        fields = '__all__'

@admin.register(Faculty)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['Fid','Fname','Fdate','Bid','Cid']
    class Meta:
        model = Faculty
        fields = '__all__'

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['Cid','Cname']  #,'Cdetail','Bid'
    class Meta:
        model = Course
        fields = '__all__'
@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['Bid', 'Bname', 'Bhod']
    class Meta:
        model = Branch
        fields = '__all__'

# Register your models here.
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display=['Marks','Sid','Cid']
    class Meta:
        model = Result
        fields = '__all__'