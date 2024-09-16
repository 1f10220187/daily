from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import DailyForm,CommentForm
from .models import Daily,Comment
import datetime
from django.db.models.functions import Length
from django.db.models import Count
# Create your views here.

def frontpage(request):
    sort= request.GET.get('sort', 'desc')
    if sort == 'desc':
        dailies = Daily.objects.all().order_by('-created_at')
    elif sort == 'asc':
        dailies = Daily.objects.all().order_by('created_at')
    elif sort == 'comments':
        dailies = Daily.objects.annotate(comment_count=Count('comments')).order_by('-comment_count')
    elif sort == 'length':
        dailies = Daily.objects.annotate(content_length=Length('content')).order_by('-content_length')
    else:
        dailies = Daily.objects.all().order_by('-created_at')
    return render(request,"daily/frontpage.html",{"dailies":dailies,"current_sort": sort})

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
    comments = daily.comments.all()
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