from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponseBadRequest

from .forms import signUpForm, User
from .utils import send_confirmation_email
from .token import confirm_mail_token_generator


def signup(request):
    if request.method == "POST":
        form = signUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            send_confirmation_email(request, user)
            return render(request, 'registration/signup_success.html')
    else:
        form = signUpForm()

    return render(request, 'registration/signup.html', {'form': form})


def activate_email(request, uid, token):
    user = get_object_or_404(User, pk=uid)
    if confirm_mail_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        return redirect('login')
    else:
        return HttpResponseBadRequest('Bad Token')
