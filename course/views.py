from django.shortcuts import render

# Create your views here.
def courseone(request):
    return render(request,'course/courseone.html')
def coursetwo(request):
    return render(request,'course/coursetwo.html')
