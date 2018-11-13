# accounts/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path('', views.SignUp.as_view(), name='signup'),
    path('upload_file', views.file_upload, name='FileUpload'),
]