
from django.urls import include, path
from .views import job_detail, post_job

urlpatterns = [
    path('post-job/', post_job, name='post_job'),
    path('job/<int:pk>/', job_detail, name='job_detail'),
    
]