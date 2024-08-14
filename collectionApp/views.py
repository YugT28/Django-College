from django.shortcuts import render
from .models import Student,Faculty,Course,Branch,Result
from .forms import Branch_Choise,Course_Choise,Student_Roll,ResultForm
import mysql.connector as con

# Create your views here.
def show(requests):
    # data=Branch.objects.all().values()
    # data=Course.objects.select_related('Bid').all().iterator()
    # data=Course.objects.raw("SELECT  Cid FROM college.collectionapp_branch join college.collectionapp_course;")
    # for i in data:
    #     print(i.Bid.Bid)
    # print()
    # for i in data:
    #     print(i.Bid.Bid)
    # print(list(data))

    # data=Student.objects.all().values()
    # print(data)

    data=Faculty.objects.filter(Bid=1)

    return render(requests,"collectionApp/show.html",context={'data':list(data)})


def student(r):
    return render(r,'student/student.html')
def student_filter(requests):
    choise=Branch_Choise()
    data=None
    if requests.method=='POST':
        choise=Branch_Choise(requests.POST)
        if choise.is_valid():
            branch_choise=int(choise.cleaned_data['branch_choise'])
            if branch_choise!= 0:
                data = Student.objects.filter(Bid=branch_choise)
            else:
                data = list(Student.objects.all().values())
    else:
        data = list(Student.objects.all().values())
    return render(requests,template_name='collectionApp/Filters/Branch_Student.html',context={'choise':choise,'data':data})


def faculty(r):
    return render (r,"faculty/faculty.html")
def faculty_filter(requests):
    choise=Branch_Choise()
    data=None
    if requests.method=='POST':
        choise=Branch_Choise(requests.POST)
        if choise.is_valid():
            branch_choise=int(choise.cleaned_data['branch_choise'])
            if  branch_choise!= 0:
                data = Faculty.objects.filter(Bid=branch_choise)
            else:
                data = Faculty.objects.all()
    else:
        data = Faculty.objects.all()

    print(dir(data))

    return render(requests,template_name='faculty/faculty_filter.html',context={'choise':choise,'data':data})

def addResult(r):
    form=ResultForm()
    mycon = con.connect(user='root', password='root', database='college', host='localhost')

    if r.method=='POST':
        form=ResultForm(r.POST)
        if form.is_valid():
            value=form.cleaned_data
            course_id=value['Cid'].Cid
            student_id=value['Student_Roll']
            marks=value['Marks']
            print(value)
            query = f'INSERT INTO college.collectionapp_result(Cid_id,Sid_id,Marks)VALUES ({course_id},{student_id},{marks})   '
            cursor = mycon.cursor()
            cursor.execute(query)
            mycon.commit()
            mycon.close()

    return render(r,"Faculty/addResult.html",context={'form':form})

def result_filter_course(requests):
    course_choise=Course_Choise()
    data=None
    tag=False
    if requests.method=='POST':
        course_choise=Course_Choise(requests.POST)
        if course_choise.is_valid():
            course_id=int(course_choise.cleaned_data['course_choise'])
            if course_id != 0:
                data=Result.objects.filter(Cid=course_id)
                tag=True
            else:
                data = Result.objects.all()
                tag=False
    else:
        data = Result.objects.all()
    return render(requests,"collectionApp/Filters/Result_Filter.html",context={'course_choise':course_choise,'data':data,'tag':tag})



def result_filter_branch(requests):
    query = '''
    with t as (SELECT Result.Sid_id,Course.Bid_id,avg(Marks) over(partition by Sid_id) as Percentage
    FROM college.collectionapp_result Result
    INNER JOIN college.collectionapp_course Course
    ON Result.Cid_id=Course.Cid)
    select Sid_id,Bid_id,max(Percentage) from t 
    group by Sid_id,Bid_id;'''
    choise=Branch_Choise()
    tag=True
    mycon=con.connect(user='root',password='root',database='college',host='localhost')
    if requests.method == 'POST':
        choise=Branch_Choise(requests.POST)
        if choise.is_valid():
            branch_choise=int(choise.cleaned_data['branch_choise'])
            if branch_choise != 0:
                cursor=mycon.cursor()
                f=cursor.execute(query)
                x=cursor.fetchall()
                y=list(filter(lambda x:True if x[1]==branch_choise else False ,x))
                z=[]
                for i in range(len(y)):
                    a=Result.objects.filter(Sid_id=y[i][0])[0].Sid.Sname
                    z.append([y[i][0],a,float(y[i][2])])
                    tag=False
            else:
                cursor = mycon.cursor()
                f = cursor.execute(query)
                x = cursor.fetchall()
                y = list(filter(lambda x: True, x))
                z = []
                for i in range(len(y)):
                    a = Result.objects.filter(Sid_id=y[i][0])[0].Sid.Sname
                    b = Result.objects.filter(Sid_id=y[i][0])[0].Cid.Bid.Bname
                    z.append([y[i][0],a, b, float(y[i][2])])
                    tag=True

    else:
        cursor = mycon.cursor()
        f = cursor.execute(query)
        x = cursor.fetchall()
        y = list(filter(lambda x:True, x))
        z = []
        for i in range(len(y)):
            a = Result.objects.filter(Sid_id=y[i][0])[0].Sid.Sname
            b = Result.objects.filter(Sid_id=y[i][0])[0].Cid.Bid.Bname
            z.append([y[i][0],a,b,float(y[i][2])])
            tag=True


    return render(requests,"collectionApp/Filters/Result_Filter_Branch.html",context={'data':z,'choise':choise,'tag':tag})

def result_filter_student(requests):
    roll=Student_Roll()
    course_choise = Course_Choise()
    data=None
    if requests.method=='POST':
        roll=Student_Roll(requests.POST)
        course_choise=Course_Choise(requests.POST)
        if roll.is_valid() and course_choise.is_valid():
            student_roll=int(roll.cleaned_data['student_roll'])
            course_choise_number=int(course_choise.cleaned_data['course_choise'])
            if course_choise_number==0:
                data=Result.objects.filter(Sid_id=student_roll)
            else :
                data = Result.objects.filter(Sid_id=student_roll,Cid_id=course_choise_number)
    print(dir(data))
    return  render(requests,"collectionApp/Filters/Result_Filter_Student.html",context={'student_id':roll,'course_choise':course_choise,'data':data})


def result(requests):
    return render(requests,'Result/result.html')








def showcourse(request):
    X=Course.objects.all()
    return render(request,'course/showCourse.html',context={'data':X})



