from django import forms
# from django.forms import CharField, PasswordInput, DateTimeField

from prepareDjango.apps.web.models import User


class LoginForm(forms.ModelForm):
    # username = CharField(max_length=10)
    # password = CharField(max_length=10, widget=PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']

    def is_valid(self):
        is_valid = super().is_valid()
        if is_valid:
            username = self.cleaned_data['username']
            if not username.startswith("usr_"):
                is_valid = False
                self.add_error("username", "username should start with usr")
        return is_valid
