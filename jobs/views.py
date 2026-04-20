from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import JobForm
from .models import Job
from django.shortcuts import get_object_or_404
from .models import Job, Application

@login_required
def post_job(request):
    # Check karein ki user Employer hai ya nahi
    if not request.user.is_employer:
        return redirect('home') # Sirf recruiters allow hain
        
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect('home')
    else:
        form = JobForm()
    return render(request, 'jobs/post_job.html', {'form': form})

# Home page par saari jobs dikhane ke liye update karein
def home(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'jobs': jobs})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    # Check karein ki kya user ne pehle hi apply kar diya hai
    has_applied = False
    if request.user.is_authenticated:
        has_applied = Application.objects.filter(job=job, user=request.user).exists()
    
    return render(request, 'jobs/job_detail.html', {
        'job': job,
        'has_applied': has_applied
    })