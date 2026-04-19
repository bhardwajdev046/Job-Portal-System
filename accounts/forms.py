from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegistrationForm(UserCreationForm):
    # User se poochne ke liye ki wo kaun hai
    CHOICES = [('candidate', 'Candidate (Job Seeker)'), ('employer', 'Employer (Recruiter)')]
    user_type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="I am a...")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user_type = self.cleaned_data.get('user_type')
        if user_type == 'candidate':
            user.is_candidate = True
        elif user_type == 'employer':
            user.is_employer = True
        if commit:
            user.save()
        return user