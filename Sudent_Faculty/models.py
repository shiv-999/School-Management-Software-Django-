from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

TYPE = (
    ('MECH', 'MECH'),
    ('ELECTRICAL', 'ELECTRICAL'),
    ('CHEM', 'Chemical'),
    ('IT', 'IT'),
    ('CSE', 'CSE')
)
Sub=(
    ("TOC","TOC"),
    ("PYTHON","PYTHON"),
    ("SOFTWARE ENGINEERING","SOFTWARE ENGINEERING"),
    ("OS","OS"),
    ("DBMS","DBMS")
    
)
Stud=(
    ("FY","FY"),
    ("SY","SY"),
    ("TY","TY"),
    ("BTECH","BTECH")
)

class Student_info(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    Studentname= models.CharField(max_length=60)
    image = models.ImageField()
    RegNO=models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    Taluka=models.CharField(max_length=15)
    District=models.CharField(max_length=15)
    pincode=models.IntegerField()
    
    def __str__(self):
        return '%s--%s'% (self.Studentname,self.RegNO)
    # def __str__(self):
    #     return '%s'% (self.RegNO)
    


class Admission(models.Model):
   
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    regNO = models.ForeignKey(Student_info,on_delete=models.CASCADE,related_name='RegNO_Student_set')
    nameStudent= models.ForeignKey(Student_info,on_delete=models.CASCADE,related_name='Studentname_Student_set')
    Class=models.CharField(max_length=20,choices=Stud)
    branch=models.CharField(max_length=20, choices=TYPE)
    Year=models.IntegerField(default=2022)
    Date_Admission=models.DateTimeField()
    Semester=models.CharField(max_length=20)
    
    
    def __str__(self):
        return '%s--%s' % (self.regNO,self.nameStudent)
    # def __str__(self):
    #     return '%s' % (self.nameStudent)


class marks(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    regNO=models.ForeignKey(Student_info,on_delete=models.CASCADE)
    Totalmarks=models.IntegerField()
    Semester=models.CharField(max_length=10)
    Year=models.IntegerField()
    def __str__(self):
        return '%s' % (self.regNO)


class Stu_Feedback(models.Model):
    regNO=models.ForeignKey(Student_info,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=False, auto_now_add=True)
    Subject=models.CharField(max_length=20 ,choices=Sub)
    Feedback_stu=models.CharField(max_length=150)
        

    def __str__(self):
        return '%s' % (self.regNO)

 