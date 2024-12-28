from django import forms
# this will allow us to create custom forms

from .models import User, UserProfile 
# imported User model, UserProfile model from models.py to link the form with database

# we have created a custom from named UserRegistrationForm which is 
# inherited from forms.ModelForm
# Why ModelForm? ModelForm will automatically generates the form fields
# based corresponding to database model(User in this case)
class UserRegistrationForm(forms.ModelForm):

    # CharField is means we accept the string input
    password = forms.CharField(widget=forms.PasswordInput)

    # we've defined this class Meta to link the form with the User model
    # and specify the field to include in form.
    class Meta:
        # linking the form with User model
        model = User

        email = forms.EmailField()
        profile_picture = forms.ImageField(required=False)  
        
        # fields to include in the form
        fields = ['name', 'email', 'password', 'phone', 'address', 'role', 'profile_picture']

    # this method is used to clean the password field
    def clean_password(self):
        password = self.cleaned_data.get('password')
        return password
