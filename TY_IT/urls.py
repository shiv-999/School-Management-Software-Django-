"""Admission URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Sudent_Faculty.views import view_Student,view_home,view_Login,view_Index
from Sudent_Faculty.views import view_Admission,view_Marks,view_Feedback,view_register
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Sudent_Faculty.views import Chart_data
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/', view_home,name='home'),
    path('Login/', view_Login,name='Login'),
    path('Index/', view_Index,name='Index'),
    
    path('Student/', view_Student),
    path('Admission/', view_Admission),
    path('Mark/', view_Marks),
    path('Feedback/', view_Feedback),    
    path('register/', view_register,name="add_student"),  
    path('Chart',Chart_data.as_view(),name='Chart')
]
urlpatterns += staticfiles_urlpatterns()
