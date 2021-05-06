from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

#custom user creation form
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)

#custom user update form
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)