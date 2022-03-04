from .models import NewUser
from django.contrib.auth.forms import UserCreationForm

class NewUserForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ['username', 'email', 'group', 'department','password1', 'password2']
    def save(self, commmit=True):
        user = super(NewUserForm, self)
        user.save()
        return user