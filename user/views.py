from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username}! Now you can log in')
            return redirect('blog-login')

    else:
       form = UserRegisterForm()  # inbuilt form in class
    return render(request, 'user/register.html', {'form': form})


@login_required
def profile(request):
   if request.method == 'POST':
      u_form = UserUpdateForm(request.POST, instance=request.user)
      p_form = ProfileUpdateForm(request.POST,
      request.FILES,
      instance=request.user.profile)

      if u_form.is_valid() and p_form.is_valid():
          u_form.save()
          p_form.save()
          messages.success(
                request, f'Your profile has been updated')
      return redirect('blog-profile')

   else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
   context ={
        'u_form': u_form,
        'p_form': p_form
      }
   return render(request,'user/profile.html',context)





