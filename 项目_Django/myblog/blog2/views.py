from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    # return HttpResponse('Hello,World!')
    return render(request,'blog2/index.html',{'blog':'This is a Blog2!'})

