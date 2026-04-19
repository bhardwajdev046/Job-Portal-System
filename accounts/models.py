from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. Main User Model
class User(AbstractUser):
    # Boolean fields se hum pehchanenge ki user Candidate hai ya Employer
    is_employer = models.BooleanField(default=False)
    is_candidate = models.BooleanField(default=False)

    def __str__(self):
        return self.username

# 2. Candidate Profile (Jo Job dhoond rahe hain)
class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidate_profile')
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True)
    skills = models.TextField(blank=True, help_text="Enter skills separated by commas")
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

# 3. Employer Profile (Jo Job de rahe hain)
class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employer_profile')
    company_name = models.CharField(max_length=200)
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.company_name