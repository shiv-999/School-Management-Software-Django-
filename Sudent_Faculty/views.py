from django.shortcuts import render,redirect
from django.views import View
from .models import Student_info,Admission,marks,Stu_Feedback
from django.views.generic import TemplateView
# Create your views here.
def view_home(request):
    return render(request,'home.html',{})
def view_Login(request):
    return render(request,'Login.html',{})
def view_Index(request):
    return render(request,'index.html',{})

def view_Student(request):
    stu1=Student_info.objects.all()
    
    
    return render(request,'Student.html',{'s':stu1})

def view_Admission(request):
    Addm=Admission.objects.all()
    
    return render(request,'Admiss.html',{'ad':Addm})

def view_Marks(request):
    mar=marks.objects.all()
    
    return render(request,'Total_marks.html',{'mk':mar})
def view_Feedback(request):
    feed=Stu_Feedback.objects.all()
    
    return render(request,'Feedback.html',{'fd':feed})
def view_register(request):
    if(request.method=="POST"):
        Studentname=request.POST.get('Studentname')
        RegNO=request.POST.get('RegNO')
        image=request.POST.get('image')
        address=request.POST.get('address')
        Taluka=request.POST.get('Taluka')
        District=request.POST.get('District')
        pincode=request.POST.get('pincode')
        
        
        student = Student_info(
            Studentname=Studentname,
            image=image,
            RegNO=RegNO,
            address=address,
            Taluka=Taluka,
            District=District,
            pincode=pincode
        )
        
        student.save();
        return render(request,"home.html",)
    
    return render(request,"register.html",{})
def index(request):
    return render(request,'index.html')

class Chart_data(TemplateView):
    template_name='Sudent_Faculty/chart.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] =Student_info.objects.all() 
        return context

    