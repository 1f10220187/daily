from django.urls import path

from daily.views import frontpage

urlpatterns = [
    path('',frontpage)
]