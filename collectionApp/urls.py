from django.urls import path
from .views import show,student_filter,faculty_filter,result_filter_course,result_filter_branch,result_filter_student,result,showcourse,faculty,addResult,addStudent
urlpatterns = [
    path('show/',show,name="show"),
    path('student_filter/',student_filter, name="student_filter"),
    path('faculty/faculty_filter/', faculty_filter, name="faculty_filter"),
    path('faculty/addResult/',addResult,name='addResult'),
    path('faculty/addStudent/',addStudent,name='addStudent'),
    path("faculty/",faculty,name='faculty'),

    path('result/result_filter_course/', result_filter_course, name="result_filter_course"),
    path('result/result_filter_branch/', result_filter_branch, name="result_filter_branch"),
    path('result/result_filter_student/', result_filter_student, name="result_filter_student"),
    path("result/",result,name="result"),
    path("showCourse/",showcourse,name='showcourse'),


]