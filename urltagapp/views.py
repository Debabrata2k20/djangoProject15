from django.shortcuts import render
# Create your views here.
def home_view(request):
    return render(request,'home.html')
def nav_view(request):
    return render(request,'nav.html')