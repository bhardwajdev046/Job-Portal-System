from django.contrib import admin
from django.urls import path, include
from jobs import views as job_views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. Accounts (Login, Register, Logout)
    path('accounts/', include('accounts.urls')),
    
    # 2. Jobs (Post Job, Job Details, etc.)
    path('jobs/', include('jobs.urls')), 
    
    # 3. Home Page
    path('', job_views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)