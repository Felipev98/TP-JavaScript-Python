from django import forms
from .models import Customer, Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)

    def save(self, commit=False):
        user = super().save(commit=True)
        Customer.objects.create(user=user, name=self.cleaned_data['username'], email=self.cleaned_data['email'])
        return user
