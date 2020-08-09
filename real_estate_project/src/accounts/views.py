from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect

from .forms import SignUpForm
from django.contrib import messages
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, """Thank you!
Your registration successfully. please login""")
            return redirect('/login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})



   