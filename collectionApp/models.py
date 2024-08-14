from django.db import models



class Branch(models.Model):
    Bid=models.IntegerField(primary_key=True)
    Bname=models.CharField(max_length=30)
    Bhod=models.CharField(max_length=30)

    def __str__(self):
        return str(self.Bname)

class Course(models.Model):
    Cid=models.IntegerField(primary_key=True)
    Cname=models.CharField(max_length=30)
    Cdetail=models.TextField()
    Bid=models.ForeignKey("Branch",on_delete=models.CASCADE,null=True)
    def __str__(self):
        return str(self.Cname)






class Faculty(models.Model):
    Fid=models.IntegerField(primary_key=True)
    Fname=models.CharField(max_length=30)
    Fdate=models.DateField()
    Bid=models.ForeignKey("Branch",on_delete=models.CASCADE)
    Cid=models.ForeignKey("Course",on_delete=models.SET_NULL,null=True)

class Student(models.Model):
    Sid=models.IntegerField(primary_key=True)
    Sname=models.CharField(max_length=30)
    Sdob=models.DateField()
    Syear=models.SmallIntegerField()
    Bid=models.ForeignKey("Branch",on_delete=models.CASCADE,null=True)
    def __str__(self):
        return str(self.Sname)




class Result(models.Model):
    Cid = models.ForeignKey("Course", on_delete=models.CASCADE, null=True)
    Sid = models.ForeignKey("Student", on_delete=models.CASCADE, null=True)
    Marks=models.SmallIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['Cid', 'Sid'], name='unique_Cid_Sid')
        ]

