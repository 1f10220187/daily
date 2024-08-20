from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DailyForm
from .models import Daily
# Create your views here.

def frontpage(request):
    dailies=Daily.objects.all()
    return render(request,"daily/frontpage.html",{"dailies":dailies})

def create_entry(request):
    if request.method == "POST":
        form = DailyForm(request.POST)
        if form.is_valid():
            daily = form.save(commit=False)
            daily.save()
            return redirect("frontpage")
    else:
        form = DailyForm()
    return render(request, "daily/create.html",{"form":form})