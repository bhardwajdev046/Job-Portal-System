from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company_name', 'location', 'job_type', 'salary_range', 'description', 'requirements']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Job ki details yahan likhein...'}),
            'requirements': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Requirements points mein likhein...'}),
        }