from django.shortcuts import render, redirect

from .forms import signUpForm


def signup(request):
    if request.method == "POST":
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = signUpForm()

    return render(request, 'registration/signup.html', {'form': form})
