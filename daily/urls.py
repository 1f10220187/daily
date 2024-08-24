from django.urls import path

from daily.views import frontpage, create_daily, delete, detail

urlpatterns = [
    path('',frontpage,name='frontpage'),
    path('create',create_daily,name='create_daily'),
    path('delete/<int:id>',delete,name='delete'),
    path('detail/<int:id>',detail,name='detail'),
]