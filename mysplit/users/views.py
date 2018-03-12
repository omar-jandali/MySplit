from django.shortcuts import render

from general.models import Profile, Request, Friend, UserActivity, Privacy
from general.forms import LoginForm, SignupForm, ProfileForm, VerifyPersonalForm
from general.forms import VerifyBusinessForm, AccountUpdateForm, UserUpdateForm
from general.forms import InfoUpdateForm, PasswordUpdateForm, PrivacyUpdateForm

# the users login  view
def user_login(request):
    # check if the form was submitted
    if request.method == 'POST':
        # grab the form
        form = LoginForm(request.POST)
        # validation of the form
        if form.is_valid():
            # cleaned up data from form
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            # authenticate with the user record
            user = authenticate(username=username, password=password)
            # check if login credentials are authentic
            if user:
                # login the user to django session
                login(request, user)
                return redirect('groups')
            else:
                # re-display form with error message
                # the same form
                form = LoginForm()
                # the error
                error = 'Invalid Username/Password'
                # template parameters to display
                parameters = {
                    'form':form,
                    'error':error
                }
                # re-render the template
                return render(request, 'users/login.html', parameters)
    else:
        # display the form for submission
        form = LoginForm()
        # the template parameters
        parameters = {
            'form':form,
        }
        # render the login template
        return render(request, 'users/login.html', parameters)
