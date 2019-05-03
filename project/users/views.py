from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    # If POST request obtain instantiate form with POST data
    # Else instiantate an empty form through GET request
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        # If form is valid, save user and redirect
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Account created for {username}! You may login now."
            )
            return redirect("login")
        else:
            messages.info(request, f"ERROR")
    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {"form": form})


# Adds functionality
@login_required
def profile(request):
    if request.method == "POST":
        # Keep instances set, pass in POST data
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # Get profile image files as welll
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request, f"Account has been updated!")
            return redirect("blog-home")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"u_form": u_form, "p_form": p_form}
    return render(request, "users/profile.html", context)


# List of messages
# messages.debug
# messages.info
# messages.success
# messages.debug
# messages.error
