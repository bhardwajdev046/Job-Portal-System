
from django.urls import include, path

from accounts import views
from .views import apply_job, apply_job, candidate_dashboard, employer_dashboard, job_detail, post_job
    
urlpatterns = [
    path('post-job/', post_job, name='post_job'),
    path('job/<int:pk>/', job_detail, name='job_detail'),
    path('job/<int:pk>/apply/', apply_job, name='apply_job'),
    path('dashboard/', employer_dashboard, name='employer_dashboard'),
    path('my-applications/', candidate_dashboard, name='candidate_dashboard'),
]