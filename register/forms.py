from .models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'phone', 'gender', 'password', 'hobby')

