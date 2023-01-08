from django.shortcuts import render

# Create your views here.
def cdndownload(request):
    return render(request,'cdndownload.html')