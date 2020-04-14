
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

def must_be_unique(value):
    user = User.objects.filter(email=value)
    if len(user) > 0:
        raise forms.ValidationError("Email Already Exists")
    # Always return the cleaned data, whether you have changed it or
    # not.
    return value

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        validators=[must_be_unique]
        )

    class Meta:
        model = User
        fields = ("username", "first_name", "email", 
                  "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class RecipeForm(forms.Form):
    recipe_name = forms.CharField(max_length=50)
    recipe_time = forms.IntegerField()
    recipe_description = forms.Textarea()
    recipe_ingredients = forms.Textarea()
    recipe_instructions = forms.Textarea()

    def save(self):
        recipe_instance = models.RecipeModel()
        recipe_instance.recipe_name = self.cleaned_data["recipe_name "]
        recipe_instance.recipe_time = self.cleaned_data["recipe_time"]
        recipe_instance.recipe_description = self.cleaned_data["recipe_description"]
        recipe_instance.recipe_ingredients = self.cleaned_data["recipe_ingredients"]
        recipe_instance.recipe_instructions = self.cleaned_data["recipe_instructions"]
        recipe_instance.save()
        return recipe_instance