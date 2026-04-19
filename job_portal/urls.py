from django.contrib import admin
from django.urls import path, include
from jobs import views as job_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. Accounts (Login, Register, Logout)
    path('accounts/', include('accounts.urls')),
    
    # 2. Jobs (Post Job, Job Details, etc.)
    path('jobs/', include('jobs.urls')), 
    
    # 3. Home Page
    path('', job_views.home, name='home'),
]