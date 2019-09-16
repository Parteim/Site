from django.shortcuts import render, redirect
from .forms import CustomUserCreation, ProfileImage, CustomUserChange
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreation(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f'Пользователь {first_name} успешно зарегистрирован!')
            return redirect('sign_in')

    else:
        form = CustomUserCreation()

    return render(request, 'user/sign_up.html', {'form': form, 'title': 'Регистрация'})


@login_required
def profile_user(request):
    return render(request, 'user/profile.html')

@login_required
def change_profile(request):
    if request.method == 'POST':
        img_profile = ProfileImage(request.POST, request.FILES, instance=request.user.profile)
        change_info = CustomUserChange(request.POST, instance=request.user)

        if change_info.is_valid() and img_profile.is_valid():
            change_info.save()
            img_profile.save()
            messages.success(request, f'Данные обновлены')
            return redirect('profile')

    else:
        img_profile = ProfileImage()
        change_info = CustomUserChange(instance=request.user)
    data = {
        'img_profile': img_profile,
        'change_info': change_info,
    }
    return render(request, 'user/change_profile.html', data)
