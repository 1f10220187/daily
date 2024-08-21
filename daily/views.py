from django.shortcuts import render, redirect
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