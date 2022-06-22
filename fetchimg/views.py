from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ImgForm
from .models import GalleryDb
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
def Home(request):
    form=ImgForm()
    gal=GalleryDb.objects.all()
    context={'form':form,'galtxt':gal}
    if request.method=='POST':
        form=ImgForm(request.POST,request.FILES)
        if form.is_valid():  
            form.save()
            # return redirect('home')
    return render(request,'index.html',context)

@api_view(['POST'])
