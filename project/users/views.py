from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    # If POST request obtain instantiate form with POST data
    # Else instiantate an empty form through GET request
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # If form is valid, save user and redirect
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You may login now.' )
            return redirect('login')
        else:
            messages.info(request, f'ERROR')
    else: 
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

# Adds functionality
@login_required
def profile(request):
    return render(request, 'users/profile.html')

# List of messages
# messages.debug
# messages.info
# messages.success
# messages.debug
# messages.error