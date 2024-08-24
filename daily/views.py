from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import DailyForm
from .models import Daily
import datetime
# Create your views here.

def frontpage(request):
    dailies=Daily.objects.all()
    return render(request,"daily/frontpage.html",{"dailies":dailies})

def create_daily(request):
    if request.method == "POST":
        form = DailyForm(request.POST)
        if form.is_valid():
            daily = form.save(commit=False)
            daily.created_at=datetime.datetime.now()
            daily.save()
            return redirect('frontpage')
    else:
        form = DailyForm()
    return render(request, "daily/create.html",{"form":form})

def delete(request,id):
    daily = get_object_or_404(Daily,id=id)
    if request.method=='POST':
        daily.delete()
        return redirect(frontpage)
    dailies=Daily.objects.all()
    return render(request,"daily/frontpage.html",{"dailies":dailies})

def detail(request,id):
    daily = get_object_or_404(Daily,id=id)
    return render(request,'daily/detail.html',{'daily':daily})