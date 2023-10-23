from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, Student


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = Student
        fields = ['name',  'email', 'password1', 'password2']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = Student
        fields = ['avatar', 'name',  'email', 'bio']
