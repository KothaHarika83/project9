from django.shortcuts import render

# Create your views here.
def ifelsecondition(request):
    d={'a':100,'b':300}
    return render(request,'ifelsecondition.html')