from django.shortcuts import render

# Create your views here.

def feesone(request):
    return render(request,'fees/feesone.html')
def feestwo(request):
    return render(request,'fees/feestwo.html')
