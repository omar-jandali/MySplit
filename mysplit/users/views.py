from django.shortcuts import render

from general.models import Profile, Request, Friend, UserActivity, Privacy
from general.forms import LoginForm, SignupForm, ProfileForm, VerifyPersonalForm
from general.forms import VerifyBusinessForm, AccountUpdateForm, UserUpdateForm
from general.forms import InfoUpdateForm, PasswordUpdateForm, PrivacyUpdateForm

def test(request):
    return render(request, 'general/test.html')
