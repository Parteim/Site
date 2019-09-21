from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Profile, StudentProfile
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password


class CustomUserCreation(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'who_is')


class CustomUserChange(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name')
    #     widgets = {
    #         'email': forms.TextInput(attrs={'class': 'entry__item'}),
    #         'first_name': forms.TextInput(attrs={'class': 'entry__item'}),
    #         'last_name': forms.TextInput(attrs={'class': 'entry__item'}),
    #     }
    #
    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password2'] != cd['password']:
    #         raise ValidationError("Пароли не совпадают")
    #     return cd['password2']


class UserEmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()

        try:
            user = user_model.objects.get(email__iexact=username)
            if check_password(password, user.password):
                return user
            else:
                return None

        except user_model.DoesNotExist:
            return None


class ProfileImage(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileImage, self).__init__(*args, **kwargs)
        self.fields['img'].widget.attrs['class'] = 'upload_img'
        # self.fields['img'].label = 'Изображение профиля:'
        # self.fields['faculty'].label = 'Специальность:'
        # self.fields['age'].label = 'Возрост:'
        # self.fields['course'].label = 'Курс:'
        # self.fields['who_is'].label = 'Кем являетесь:'

    class Meta:
        model = Profile
        fields = ['img']


class StudentProfileChange(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentProfileChange, self).__init__(*args, **kwargs)
        self.fields['age'].widget.attrs['class'] = 'age'
        self.fields['age'].widget.attrs['placeholder'] = 'Возрост'
        self.fields['age'].label = 'Возрост'
        self.fields['course'].widget.attrs['class'] = 'course'
        self.fields['course'].widget.attrs['placeholder'] = 'Курс'
        self.fields['course'].label = 'Курс'
        self.fields['faculty'].widget.attrs['class'] = 'faculty'
        self.fields['faculty'].widget.attrs['placeholder'] = 'Специальность'
        self.fields['faculty'].label = 'Специальность'

    class Meta:
        model = StudentProfile
        fields = ['age', 'course', 'faculty']
