from django.shortcuts import render
from .models import course,school

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def firstPageView(request):
    return HttpResponse('Notre première page')

def my_view(request):
    return render(request, 'website/index.html', {'Courses': course.objects.all(),'Schools':school.objects.all()})
def about(request):
    return render(request, 'website/about.html', {'Courses': course.objects.all()})
def contactus(request):
    return render(request,'website/contactus.html', {'Courses': course.objects.all()})
def JoinUs(request):
    return render(request,'website/JoinUs.html', {'Courses': course.objects.all()})
def Karate(request):
    return render(request,'website/Karate.html', {'Courses': course.objects.all()})
def Judo(request):
    return render(request,'website/Judo.html', {'Courses': course.objects.all()})
def Kungfu(request):
    return render(request,'website/Kungfu.html', {'Courses': course.objects.all()})
