from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import DailyForm,CommentForm
from .models import Daily,Comment
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
    comments = daily.comment_set.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.daily = daily
            comment.save()
            return redirect('detail', id=id)
    else:
        form = CommentForm()
    return render(request,'daily/detail.html',{'daily':daily,'comments': comments, 'form': form})

def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    if request.method == 'POST':
        comment.delete()
        return redirect('detail', id=comment.daily.id)
    return redirect('frontpage')