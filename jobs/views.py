from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import JobForm
from .models import Job

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