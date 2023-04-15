from django.contrib.auth.forms import UserCreationForm

from account.models import Shopper

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Shopper
        fields = ('email',)
